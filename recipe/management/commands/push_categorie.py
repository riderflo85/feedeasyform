import os, json
from django.core.management.base import BaseCommand

from recipe.models import CategorieRecipe


class Command(BaseCommand):
    """
    This manage.py command is used to add the categorie
    recipe data in the .json file in the database.
    """
    help="Ajout des catégories de recette dans la base de données."

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
        json_file_path = directory + 'categorie_dev_data.json'

        try:
            with open(json_file_path, 'r') as jsonfile:
                data = json.load(jsonfile)
                
                for categorie in data:
                    new_categ = CategorieRecipe()
                    new_categ.name = categorie['name']
                    new_categ.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(categorie['name'])} ajouté à la base de données"
                        )
        
        except:
            self.stderr.write(self.style.ERROR('Une erreur est survenu. \
\nIl est possible que les informations existe déjà dans la base de données.'))
