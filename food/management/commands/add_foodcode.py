import os, csv
from django.core.management.base import BaseCommand

from ...models import Food


class Command(BaseCommand):
    """
    This manage.py command is used to add the food code
    present in the .csv file in th database.
    """
    help = "Ajout des code aliemtns des ingrédients dans la base de données."

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

        foods_not_found = []

        with open(csvfile_path, newline='') as csvfile:
            foods = csv.DictReader(csvfile)

            for food in foods:
                name_food_parsed = food['alim_nom_fr'].replace(' et ', ' & ')
                try:
                    f = Food.objects.get(name=name_food_parsed)
                    if f.food_code != int(food["alim_code"]):
                        f.food_code = int(food["alim_code"])
                        f.save()
                        if kwargs['verbose']:
                            self.stdout.write(
                                f"{self.style.SUCCESS(name_food_parsed)} \
modifié"
                            )
                except Food.DoesNotExist:
                    foods_not_found.append(
                        {"name": name_food_parsed, "f_code": food["alim_code"]}
                    )
        if len(foods_not_found) > 0:
            self.stderr.write(self.style.ERROR(f"\nIl y a \
{len(foods_not_found)} ingrédients qui n'ont pas été trouvés.\n"))
            self.stderr.write(self.style.ERROR(foods_not_found))
