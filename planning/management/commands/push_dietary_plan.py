import os, json
from django.core.management.base import BaseCommand

from planning.models import DietaryPlan


class Command(BaseCommand):
    """
    This manage.py command is used to add the dietary plan
    data in the .json file in the database.
    """
    help="Ajout des régimes alimentaire dans la base de données."

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
        json_file_path = directory + 'dietary_plan.json'

        try:
            with open(json_file_path, 'r') as jsonfile:
                data = json.load(jsonfile)

                for diet in data:
                    new_diet = DietaryPlan(
                        name=diet['name'],
                        description=diet['desc']
                    )
                    new_diet.save()

                    if options['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_diet)} ajouté à la base de données"
                        )

        except:
            self.stderr.write(self.style.ERROR('Une erreur est survenu. \
\nIl est possible que les informations existe déjà dans la base de données.'))