import json, os
from django.conf import settings

from recipe.models import (
    Season,
    Utensil,
    CategorieRecipe,
    Level,
    PriceScale,
    OriginRecipe,
    Recipe,
    DietaryPlan
)
from food.models import FoodGroup, Food, Allergie, StoreRack
from planning.models import MealsPerDay


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
    return [{
        "name": categ_name,
        "image_active": categ_image_active_url,
        "image_not_active": categ_image_not_active_url
    }, ...]
    """

    categs = []

    for categ in CategorieRecipe.objects.all():
        categs.append({
            "name": categ.name,
            "image_active": categ.image_active.url.replace('/media/', '/'),
            "image_not_active": categ.image_not_active.url.replace('/media/', '/')
        })

    return categs


def get_store_rack():
    """
    Get all store rack in the database.
    return [{
        "name": rack_name,
        "image_active": rack_image_active_url,
        "image_not_active": rack_image_not_active_url
    }, ...]
    """

    st_rack = []

    for rack in StoreRack.objects.all():
        st_rack.append({
            "name": rack.name,
            "image_active": rack.image_active.url.replace('/media/', '/'),
            "image_not_active": rack.image_not_active.url.replace('/media/', '/')
        })

    return st_rack

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
        diets.append({
            'name': diet.name,
            'desc': diet.description
        })

    return diets


def get_food_groups():
    """
    Get all food group in the database.
    return [{
        'name': name_food_group,
        'store_rack': store_rack_fk
    }, ...]
    """

    groups = []

    for f_g in FoodGroup.objects.all():
        try:
            name_rack = f_g.store_rack.name
        except:
            name_rack = "not defined"
        groups.append({
            'name': f_g.name,
            'store_rack': name_rack
        })

    return groups


def get_recipes(forcsvfile=False):
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
        'source': '...',
        'image': '...',
        'food': [
            {
                'name': '...',
                'quantity': '...',
            },
            ...
        ],
        'categories': [name_categorie, ...],
        'origin': '...',
        'price_scale': '...',
        'level': '...',
        'utensils': [name_utensil, ...],
        'season': [name_season, ...],
        'dietary_plan': [name_diet, ...]
    }, ...]
    """

    recipes = []

    for recipe in Recipe.objects.all().order_by('pk'):
        foods = []
        utensils = [x.name for x in recipe.utensils.all()]
        seasons = [x.name for x in recipe.season.all()]
        diets = [x.name for x in recipe.dietary_plan.all()]
        categs = [x.name for x in recipe.categories.all()]
        allergs = [x.name for x in recipe.allergies.all()]
        origin = OriginRecipe.objects.get(pk=recipe.origin.pk).name
        price_scale = PriceScale.objects.get(pk=recipe.price_scale.pk).name
        level = Level.objects.get(pk=recipe.level.pk).name

        for food in recipe.foodandquantity_set.all():
            foods.append({
                'name': food.food.name,
                'recipe_quantity': food.recipe_quantity,
                'recipe_unity': food.recipe_unity,
                'purchase_quantity': food.food_purchase_quantity,
                'purchase_unity': food.food_purchase_unity
            })
        if forcsvfile:
            c = str(categs).replace('[', "").replace(']', "").replace("'", "")
            s = str(seasons).replace('[', "").replace(']', "").replace("'", "")
            d = str(diets).replace('[', "").replace(']', "").replace("'", "")
            data = {
                'Id de la recette (non contractuel)': recipe.pk,
                'Nom de la recette': recipe.name,
                'Catégories': c,
                'Saison': s,
                'Régime alimentaire': d,
                'Ingrédients': foods,
                'Source': recipe.source,
                'Fourchette de prix': price_scale,
                'Niveau de difficulté': level,
            }
        else:
            data = {
                'name': recipe.name,
                'preparation_time': recipe.preparation_time,
                'cooking_time': recipe.cooking_time,
                'step': recipe.step,
                'tip': recipe.tip,
                'portion': recipe.portion,
                'point': recipe.point,
                'typical_recipe_city': recipe.typical_recipe_city,
                'source': recipe.source,
                'image': recipe.image.url.replace('/media/', '/'),
                'food': foods,
                'categories': categs,
                'origin': origin,
                'price_scale': price_scale,
                'level': level,
                'utensils': utensils,
                'season': seasons,
                'dietary_plan': diets,
                'allergies': allergs
            }

        recipes.append(data)
    
    return recipes


def get_foods():
    """
    Get all foods in the database.
    return [{
        'name': '...',
        'group_name': <FoodGroup>.name,
        'proteine': '...',
        'glucide': '...',
        'sucre': '...',
        'fibre': '...',
        'lipide': '...',
        'acide_gras_sature': '...',
        'cholesterol': '...',
        'sel_chlorure_de_sodium': '...',
        'potassium': '...',
        'calcium': '...',
        'magnesium': '...',
        'fer': '...',
        'zinc': '...',
        'vitamine_c': '...',
        'vitamine_d': '...',
        'vitamine_e': '...',
        'metric_unit': '...',
        'imperial_unit': '...',
    }, ...]
    """

    foods = []

    for food in Food.objects.all():
        f_data = {}
        for field, value in food.list_fields_without_verbose_name():
            if field != 'id':
                if field == 'id_group':
                    f_data['group_name'] = FoodGroup.objects.get(
                        pk=int(value)
                    ).name
                else:
                    f_data[field] = value
        foods.append(f_data)

    return foods


def get_seasons():
    """
    Get all seasons in the database.
    return [name_season, ...]
    """
    seasons = []

    for season in Season.objects.all():
        seasons.append(season.name)

    return seasons


def get_meals_per_day():
    """
    Get all meals per day in the database.
    return [{"name": name_mlp, "weight": weight_mlp}, ...]
    """
    mlps = []

    for mlp in MealsPerDay.objects.all():
        mlps.append({
            "name": mlp.name,
            "weight": mlp.weight
        })

    return mlps


def generate_json_file():
    all_data = {
        'utensils': get_utensils(),
        'recipe_categories': get_categories_recipe(),
        'levels': get_levels(),
        'price_scales': get_price_scales(),
        'seasons': get_seasons(),
        'meals_per_day': get_meals_per_day(),
        'origins_recipe': get_origins_recipe(),
        'food_groups': get_food_groups(),
        'store_racks': get_store_rack(),
        'recipes': get_recipes(),
        'diets': get_dietary_plan(),
        'foods': get_foods(),
        'allergies': [x.name for x in Allergie.objects.all()]
    }
    file_name = 'database.json'

    with open('database.json', 'w') as database_file:
        json.dump(all_data, database_file, indent=4, ensure_ascii=False)
    
    return file_name


def generate_zip_file():
    if "backup_db.zip" in os.listdir(f"{settings.MEDIA_ROOT}"):
        rm_cmd = f"rm \"{settings.MEDIA_ROOT}backup_db.zip\""
        os.system(rm_cmd)

    command = f"cd \"{settings.MEDIA_ROOT}\" && zip -r backup_db.zip recipe"
    os.system(command)
    json_file_name = generate_json_file()
    os.system(f"zip \"{settings.MEDIA_ROOT}backup_db.zip\" {json_file_name}")

    return f"{settings.MEDIA_ROOT}backup_db.zip"
