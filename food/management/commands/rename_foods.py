import os, csv
from django.core.management.base import BaseCommand

from ...models import Food, FoodGroup


class Command(BaseCommand):
    """
    This manage.py command is used to rename the food
    present in the .csv file in th database.
    """
    help = "Renome les ingrédients dans la base de données."

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Affiche chaque entrée qui sera enregistrée dans la base de données.',
        )

    def handle(self, *args, **kwargs):
        diretory = os.path.join(
            os.path.dirname(__file__),
            '../../../feedeasyform_project/assets/'
        )
        csvfile_path = diretory + 'table_src_food-plats_renamed.csv'
        food_updated = 0
        food_created = {"coutner": 0, "listing": []}
        food_not_updated = {"coutner": 0, "listing": []}

        with open(csvfile_path, newline='') as csvfile:
            foods = csv.DictReader(csvfile)

            for food in foods:
                n_f_p = food['alim_nom_fr'].replace(' et ', ' & ')
                try:
                    f = Food.objects.get(food_code=int(food["alim_code"]))
                    if f.name != n_f_p and len(f.name) > len(n_f_p):
                        f.name = n_f_p
                        f.save()
                        food_updated += 1
                        if kwargs['verbose']:
                            self.stdout.write(
                                f"{self.style.SUCCESS(f.name)} -> nom modifié"
                            )
                    else:
                        food_not_updated["coutner"] += 1
                        food_not_updated["listing"].append(f.name)

                except Food.DoesNotExist:
                    n_grp_p = food['alim_ssgrp_nom_fr'].replace(' et ', ' & ')
                    try:
                        group = FoodGroup.objects.get(name=n_grp_p)
                    except FoodGroup.DoesNotExist:
                        group = FoodGroup()
                        group.name = n_grp_p
                        group.save()

                    new_food = Food()
                    new_food.name = n_f_p
                    new_food.id_group = group
                    new_food.food_code = int(food["alim_code"])
                    new_food.proteine = food["Protéines (g/100g)"]
                    new_food.glucide = food["Glucides (g/100g)"]
                    new_food.lipide = food["Lipides (g/100g)"]
                    new_food.sucre = food["Sucres (g/100g)"]
                    new_food.fibre = food["Fibres alimentaires (g/100g)"]
                    new_food.acide_gras_sature = food["AG saturés (g/100g)"]
                    new_food.cholesterol = food["Cholestérol (mg/100g)"]
                    new_food.sel_chlorure_de_sodium = food["Sel chlorure de sodium (g/100g)"]
                    new_food.calcium = food["Calcium (mg/100g)"]
                    new_food.fer = food["Fer (mg/100g)"]
                    new_food.magnesium = food["Magnésium (mg/100g)"]
                    new_food.potassium = food["Potassium (mg/100g)"]
                    new_food.zinc = food["Zinc (mg/100g)"]
                    new_food.vitamine_c = food["Vitamine C (mg/100g)"]
                    new_food.vitamine_d = food["Vitamine D (µg/100g)"]
                    new_food.vitamine_e = food["Vitamine E (mg/100g)"]
                    new_food.energie = food["Energie (kcal/100g)"]
                    new_food.save()
                    food_created["coutner"] += 1
                    food_created["listing"].append(new_food.name)
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_food.name)} ajouté \
à la base de données")
        if kwargs['verbose']:
            self.stdout.write(self.style.WARNING(
                f"Modifié : {food_updated}\nNon Modifié : {food_not_updated}\
\nCréé : {food_created}"))