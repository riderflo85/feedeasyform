from planning.models import Utensil, CategorieRecipe, Level, PriceScale, \
    OriginRecipe, Recipe, FoodAndQuantity
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


def get_categories_utensil():
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
        'portion': '...',
        'point': '...',
        'food': [
            {
                'name_food': '...',
                'quantity': '...',
            },
            ...
        ],
        'categorie': '...',
        'origin': '...',
        'price_scale': '...',
        'level': '...',
        'utensils': '...'
    }, ...]
    """

    recipes = []

    for recipe in Recipe.objects.all():
        foods = []
        utensils = []
        categ = CategorieRecipe.objects.get(pk=recipe.categorie).name
        origin = OriginRecipe.objects.get(pk=recipe.origin).name
        price_scale = PriceScale.objects.get(pk=recipe.price_scale).name
        level = Level.objects.get(pk=recipe.level).name

        

        data = {

        }