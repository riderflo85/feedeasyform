import os, csv
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from food.models import FoodGroup, Food


class Command(BaseCommand):
    """
    This manage.py command is used to register the foods
    present in the .csv file in th database.
    """
    help = "Ajout des ingrédients dans la base de données."

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
        csvfile_path = diretory + 'table_ingredients.csv'

        try:
            with open(csvfile_path, newline='') as csvfile:
                foods = csv.DictReader(csvfile)

                for food in foods:
                    name_grp_parsed = food['alim_grp_nom_fr'].replace(' et ', ' & ')
                    try:
                        group = FoodGroup.objects.get(name=name_grp_parsed)

                    except ObjectDoesNotExist:
                        group = FoodGroup()
                        group.name = name_grp_parsed
                        group.save()
                    
                    name_food_parsed = food['alim_nom_fr'].replace(' et ', ' & ')
                    new_food = Food()
                    new_food.name = name_food_parsed
                    new_food.id_group = group
                    new_food.food_code = food["alim_code"]
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

                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(name_food_parsed)} ajouté à la base de données"
                        )
        except:
            self.stderr.write(self.style.ERROR('Une erreur est survenu. \
\nIl est possible que les ingrédients existe déjà dans la base de données.'))
