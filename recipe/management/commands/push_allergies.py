import os, json
from django.core.management.base import BaseCommand

from food.models import Allergie


class Command(BaseCommand):
    """
    This manage.py command is used to add the allergie
    data in the .json file in the database.
    """
    help="Ajout des allergies courantes dans la base de données."

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Affiche chaque entrée qui sera enregistrée dans la base de données.',
        )

    def handle(self, *args, **kwargs):
        directory = os.path.join(
            os.path.dirname(__file__),
            '../../../feedeasyform_project/assets/'
        )
        json_file_path = directory + 'allergies.json'

        try:
            with open(json_file_path, 'r') as jsonfile:
                data = json.load(jsonfile)
                
                for allergie in data:
                    new_allergie = Allergie()
                    new_allergie.name = allergie['name']
                    new_allergie.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(allergie['name'])} ajouté à la base de données"
                        )
        
        except:
            self.stderr.write(self.style.ERROR('Une erreur est survenu. \
\nIl est possible que les informations existe déjà dans la base de données.'))
