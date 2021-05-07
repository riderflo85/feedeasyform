import os, json
from django.conf import settings
from django.core.management.base import BaseCommand

from recipe.models import (
    CategorieRecipe,
    DietaryPlan,
    Level,
    OriginRecipe,
    PriceScale,
    Recipe,
    FoodAndQuantity,
    Season,
    Utensil
)
from food.models import Food, FoodGroup, Allergie
from planning.models import MealsPerDay


class Command(BaseCommand):
    """
    This manage.py command is used for restore the recipe table in database.
    Take one argument. Path to backup_db.zip zip file.
    """
    help="Restore la table Recipe de la base de données.\
        prend le chemin de l'archive zip en paramètre."

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Affiche chaque entrée qui sera engistréee dans la BDD.'
        )
        parser.add_argument('path', nargs='+', type=str)
        parser.add_argument('add_media', nargs='+', type=str)

    def handle(self, *args, **kwargs):
        self.stdout.write("Ouverture du fichier de sauvegarde et restauration \
en cours. Merci de patienter...")
        directory_path = kwargs['path'][0]
        add_media = kwargs['add_media'][0]
        if 'database.json' not in os.listdir(directory_path):
            if 'recipe' not in os.listdir(directory_path):
                cmd1 = f"cd {directory_path}"
                cmd2 = "unzip backup_db.zip"
                os.system(f"{cmd1} && {cmd2}")
                if add_media == 'add-media':
                    os.system(f"mv {directory_path}recipe \"{settings.MEDIA_ROOT}\"")

        jsonfile_path = directory_path + 'database.json'
        with open(jsonfile_path, 'r') as jsonfile:
            data = json.load(jsonfile)

            for mlp in data['meals_per_day']:
                try:
                    MealsPerDay.objects.get(name=mlp)
                except:
                    new_mlp = MealsPerDay(name=mlp)
                    new_mlp.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_mlp.name)} \
ajouté à la base de données"
                        )

            for food_group in data['food_groups']:
                try:
                    FoodGroup.objects.get(name=food_group)
                except:
                    new_f_g = FoodGroup(name=food_group)
                    new_f_g.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_f_g.name)} \
ajouté à la base de données"
                        )

            for food in data['foods']:
                try:
                    Food.objects.get(name=food['name'])
                except:
                    new_food = Food()
                    for k, v in food.items():
                        if k == 'group_name':
                            new_food.id_group = FoodGroup.objects.get(name=v)
                        else:
                            setattr(new_food, k, v)
                    new_food.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_food.name)} \
ajouté à la base de données"
                        )

            for categ in data['recipe_categories']:
                try:
                    CategorieRecipe.objects.get(name=categ['name'])
                except:
                    new_categ = CategorieRecipe()
                    new_categ.name = categ['name']
                    new_categ.image_active = categ['image_active']
                    new_categ.image_not_active = categ['image_not_active']
                    new_categ.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_categ.name)} \
ajouté à la base de données"
                        )

            for origin in data['origins_recipe']:
                try:
                    OriginRecipe.objects.get(name=origin)
                except:
                    new_origin = OriginRecipe(name=origin)
                    new_origin.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_origin.name)} \
ajouté à la base de données"
                        )

            for level in data['levels']:
                try:
                    Level.objects.get(name=level)
                except:
                    new_level = Level(name=level)
                    new_level.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_level.name)} \
ajouté à la base de données"
                        )

            for price_scale in data['price_scales']:
                try:
                    PriceScale.objects.get(name=price_scale)
                except:
                    new_p_s = PriceScale(name=price_scale)
                    new_p_s.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_p_s.name)} \
ajouté à la base de données"
                        )

            for utensil in data['utensils']:
                try:
                    Utensil.objects.get(name=utensil)
                except:
                    new_u = Utensil(name=utensil)
                    new_u.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_u.name)} \
ajouté à la base de données"
                        )

            for season in data['seasons']:
                try:
                    Season.objects.get(name=season)
                except:
                    new_s = Season(name=season)
                    new_s.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_s.name)} \
ajouté à la base de données"
                        )

            for diet in data['diets']:
                try:
                    DietaryPlan.objects.get(name=diet)
                except:
                    new_d = DietaryPlan(name=diet)
                    new_d.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_d.name)} \
ajouté à la base de données"
                        )

            for allergie in data['allergies']:
                try:
                    Allergie.objects.get(name=allergie)
                except:
                    new_a = Allergie(name=allergie)
                    new_a.save()
                    if kwargs['verbose']:
                        self.stdout.write(
                            f"{self.style.SUCCESS(new_a.name)} \
ajouté à la base de données"
                        )

            for recipe in data['recipes']:
                r_origin = OriginRecipe.objects.get(
                    name=recipe['origin']
                )
                r_price_scale = PriceScale.objects.get(
                    name=recipe['price_scale']
                )
                r_level = Level.objects.get(
                    name=recipe['level']
                )

                categories = set()
                for categ in recipe['categories']:
                    c = CategorieRecipe.objects.get(name=categ)
                    categories.add(c)

                utensils = set()
                for utensil in recipe['utensils']:
                    u = Utensil.objects.get(name=utensil)
                    utensils.add(u)

                seasons = set()
                for season in recipe['season']:
                    s = Season.objects.get(name=season)
                    seasons.add(s)

                diets = set()
                for diet in recipe['dietary_plan']:
                    d = DietaryPlan.objects.get(name=diet)
                    diets.add(d)

                try:
                    new_r = Recipe.objects.get(name=recipe['name'])
                    state = 'modifiée'
                except:
                    new_r = Recipe()
                    state = 'ajoutée'

                new_r.name = recipe['name']
                new_r.preparation_time = recipe['preparation_time']
                new_r.cooking_time = recipe['cooking_time']
                new_r.step = recipe['step']
                new_r.tip = recipe['tip']
                new_r.portion = recipe['portion']
                new_r.point = recipe['point']
                new_r.typical_recipe_city = recipe['typical_recipe_city']
                new_r.source = recipe['source']
                new_r.image = recipe['image']
                new_r.origin = r_origin
                new_r.price_scale = r_price_scale
                new_r.level = r_level
                new_r.save()

                new_r.categories.set(categories)
                new_r.utensils.set(utensils)
                new_r.season.set(seasons)
                new_r.dietary_plan.set(diets)

                for food in recipe['food']:
                    f = Food.objects.get(name=food['name'])
                    fq = FoodAndQuantity()
                    fq.food = f
                    fq.recipe = new_r
                    fq.recipe_quantity = food['recipe_quantity']
                    fq.recipe_unity = food['recipe_unity']
                    fq.food_purchase_quantity = food['purchase_quantity']
                    fq.food_purchase_unity = food['purchase_unity']
                    fq.save()

                if kwargs['verbose']:
                    self.stdout.write(
                        f"{self.style.SUCCESS(new_r.name)} {state} à la base de données"
                    )
