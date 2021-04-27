from .models import (
    Recipe,
    CategorieRecipe,
    Utensil,
    OriginRecipe,
    DietaryPlan,
    Season,
    Allergie
)


def list_all_recipe():
    recipes = []

    for recipe in Recipe.objects.all():
        recipes.append((recipe.pk, recipe.name))
    
    return recipes

def list_all_categ():
    categories = []

    for categ in CategorieRecipe.objects.all():
        categories.append((categ.pk, categ.name))

    return categories

def list_all_utensil():
    utensils = []

    for utensil in Utensil.objects.all():
        utensils.append((utensil.pk, utensil.name))
    
    return utensils

def list_all_origin_recipe():
    origins = []

    for origin in OriginRecipe.objects.all():
        origins.append((origin.pk, origin.name))

    return origins

def list_all_diet():
    diets = []

    for diet in DietaryPlan.objects.all():
        diets.append((diet.pk, diet.name))

    return diets

def list_all_season():
    seasons = []

    for season in Season.objects.all():
        seasons.append((season.pk, season.name))
    
    return seasons

def list_all_allegies():
    return [(x.pk, x.name) for x in Allergie.objects.all()]