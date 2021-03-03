import os, json
from django.core.management.base import BaseCommand

from recipe.models import Level, PriceScale


class Command(BaseCommand):
    """
    This manage.py command is used to add the recipe level
    and recipe price scale data in the .json file in the database.
    """
    help="Ajout des niveaux de difficultés et des fourchette de prix."

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Affiche chaque entrée qui sera enregistrée dans la base de données.',
        )

    def handle(self, *args, **options):
        directory = os.path.join(
            os.path.dirname(__file__),
            '../../../feedeasyform_project/assets/'
        )
        json_file_path = directory + 'level_and_price_scale.json'

        try:
            with open(json_file_path, 'r') as jsonfile:
                data = json.load(jsonfile)

                for level in data['level']:
                    new_level = Level(name=level)
                    new_level.save()
                    if options['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(level)} ajouté à la base de données"
                        )

                for price_scale in data['price_scale']:
                    new_price_scale = PriceScale(name=price_scale)
                    new_price_scale.save()
                    if options['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(price_scale)} ajouté à la base de données"
                        )
        
        except:
            self.stderr.write(self.style.ERROR('Une erreur est survenu. \
\nIl est possible que les informations existe déjà dans la base de données.'))