import json, os

from planning.models import Utensil, CategorieRecipe, Level, PriceScale, \
    OriginRecipe, Recipe, DietaryPlan
from food.models import FoodGroup


def get_utensils():
    """
    Get all utensils in the database.
    return ['name_utensil', ...]
    """

    utensils = []

    for utensil in Utensil.objects.all():
        utensils.append(utensil.name)
    
    return utensils


def get_categories_recipe():
    """
    Get all recipe categories in the database.
    return ['name_categ', ...]
    """

    categs = []

    for categ in CategorieRecipe.objects.all():
        categs.append(categ.name)

    return categs


def get_levels():
    """
    Get all level recipe in the database.
    return ['name_level', ...]
    """

    levels = []

    for level in Level.objects.all():
        levels.append(level.name)
    
    return levels


def get_price_scales():
    """
    Get all price scale recipe in the database.
    return ['name_price_scale', ...]
    """

    price_scales = []

    for p_s in PriceScale.objects.all():
        price_scales.append(p_s.name)
    
    return price_scales


def get_origins_recipe():
    """
    Get all the origin recipe in the database.
    return ['name_origin_recipe', ...]
    """

    origins = []

    for o_r in OriginRecipe.objects.all():
        origins.append(o_r.name)

    return origins


def get_dietary_plan():
    """
    Get all the dietary plan in the database.
    return ['name_diet', ...]
    """

    diets = []

    for diet in DietaryPlan.objects.all():
        diets.append(diet.name)

    return diets


def get_food_groups():
    """
    Get all food group in the database.
    return ['name_food_group', ...]
    """

    groups = []

    for f_g in FoodGroup.objects.all():
        groups.append(f_g.name)

    return groups


def get_recipes():
    """
    Get all recipes in the database.
    return [{
        'name': '...',
        'preparation_time': '...',
        'cooking_time': '...',
        'step': '...',
        'tip': '...',
        'portion': '...',
        'point': '...',
        'typical_recipe_city': '...',
        'food': [
            {
                'name': '...',
                'quantity': '...',
            },
            ...
        ],
        'categorie': '...',
        'origin': '...',
        'price_scale': '...',
        'level': '...',
        'utensils': [name_utensil, ...],
        'season': [name_season, ...],
        'dietary_plan': [name_diet, ...]
    }, ...]
    """

    recipes = []

    for recipe in Recipe.objects.all():
        foods = []
        utensils = []
        seasons = []
        diets = []
        categ = CategorieRecipe.objects.get(pk=recipe.categorie.pk).name
        origin = OriginRecipe.objects.get(pk=recipe.origin.pk).name
        price_scale = PriceScale.objects.get(pk=recipe.price_scale.pk).name
        level = Level.objects.get(pk=recipe.level.pk).name

        for utensil in recipe.utensils.all():
            utensils.append(utensil.name)

        for food in recipe.foodandquantity_set.all():
            foods.append({
                'name': food.food.name,
                'quantity': food.quantity
            })

        for season in recipe.season.all():
            seasons.append(season.name)

        for diet in recipe.dietary_plan.all():
            diets.append(diet.name)

        data = {
            'name': recipe.name,
            'preparation_time': recipe.preparation_time,
            'cooking_time': recipe.cooking_time,
            'step': recipe.step,
            'tip': recipe.tip,
            'portion': recipe.portion,
            'point': recipe.point,
            'typical_recipe_city': recipe.typical_recipe_city,
            'food': foods,
            'categorie': categ,
            'origin': origin,
            'price_scale': price_scale,
            'level': level,
            'utensils': utensils,
            'season': seasons,
            'dietary_plan': diets
        }

        recipes.append(data)
    
    return recipes


def generate_json_file():
    all_data = {
        'utensils': get_utensils(),
        'recipe_categories': get_categories_recipe(),
        'levels': get_levels(),
        'price_scales': get_price_scales(),
        'origins_recipe': get_origins_recipe(),
        'food_groups': get_food_groups(),
        'recipes': get_recipes(),
        'diets': get_dietary_plan()
    }
    file_name = 'database.json'

    if file_name not in os.listdir('.'):
        with open('database.json', 'w') as database_file:
            json.dump(all_data, database_file, indent=4, ensure_ascii=False)
    
    return file_name