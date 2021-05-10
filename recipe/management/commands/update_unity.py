from django.core.management.base import BaseCommand

from ...models import Recipe


class Command(BaseCommand):
    """
    This manage.py command is used to update the foods unity.
    """
    help = "Met à jour les unitées de la base de données."

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Affiche chaque recette qui sera mise à jour dans la base de données.',
        )

    def handle(self, *args, **kwargs):
        unit_conversion = {
            "U": "Unité",
            "GR": "Gr",
            "CL": "Cl",
            "CaC": "Cuillère à café",
            "CaS": "Cuillère à soupe",
            "Pincee": "Pincéé"
        }

        for recipe in Recipe.objects.all():
            for f_q in recipe.foodandquantity_set.all():
                if f_q.recipe_unity in unit_conversion.keys():
                    f_q.recipe_unity = unit_conversion[f_q.recipe_unity]
                if f_q.food_purchase_unity in unit_conversion.keys():
                    f_q.food_purchase_unity = unit_conversion[
                        f_q.food_purchase_unity
                    ]
                f_q.save()