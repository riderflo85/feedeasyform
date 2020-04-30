from .models import Recipe, Categorie, Utensil


def list_all_recipe():
    recipes = []

    for recipe in Recipe.objects.all():
        recipes.append((recipe.pk, recipe.name))
    
    return recipes

def list_all_categ():
    categories = []

    for categ in Categorie.objects.all():
        categories.append((categ.pk, categ.name))

    return categories

def list_all_utensil():
    utensils = []

    for utensil in Utensil.objects.all():
        utensils.append((utensil.pk, utensil.name))
    
    return utensils