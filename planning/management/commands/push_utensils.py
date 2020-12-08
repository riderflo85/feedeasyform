import os, csv
from django.core.management.base import BaseCommand

from planning.models import Utensil


class Command(BaseCommand):
    """
    This manage.py command is used to register the utensils
    present in the .csv file in th database.
    """
    help = "Ajout des ustensils de cuisine dans la base de données."

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
        csvfile_path = directory + 'table_ustensils_cuisine.csv'

        try:
            with open(csvfile_path, newline='') as csvfile:
                utensils = csv.DictReader(csvfile)

                for line in utensils:
                    utensil = Utensil(name=line['Ustensils cuisine'])
                    utensil.save()

                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(utensil)} ajouté à la base de données"
                        )

        except:
            self.stderr.write(self.style.ERROR('Une erreur est survenu. \
\nIl est possible que les ustensils existe déjà dans la base de données.'))