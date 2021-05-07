import os, json
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from food.models import FoodGroup, Food


class Command(BaseCommand):
    """
    This manage.py command is used to register the new foods
    present in the .json file in th database.
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
        jsonfile_path = diretory + 'new_foods.json'

        try:
            with open(jsonfile_path, 'r') as jsonfile:
                foods = json.load(jsonfile)

                for food in foods:
                    name_food_parsed = food.pop('name').replace(' et ', ' & ')

                    try:
                        new_food = Food.objects.get(name=name_food_parsed)
                        state = "modifié dans"
                    except ObjectDoesNotExist:
                        new_food = Food()
                        state = "ajouté à"

                    name_grp_parsed = food.pop('categorie_name').replace(' et ', ' & ')
                    food.pop('source AJOUT')

                    try:
                        group = FoodGroup.objects.get(name=name_grp_parsed)
                    except ObjectDoesNotExist:
                        group = FoodGroup()
                        group.name = name_grp_parsed
                        group.save()
                    
                    new_food.name = name_food_parsed
                    new_food.id_group = group
                    for k, v in food.items():
                        setattr(new_food, k, v)
                    new_food.save()

                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(name_food_parsed)} {state} la base de données"
                        )

        except Exception as e:
            print(e)
            self.stderr.write(self.style.ERROR('Une erreur est survenu. \
\nIl est possible que les ingrédients existe déjà dans la base de données.'))
