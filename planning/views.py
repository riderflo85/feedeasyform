from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, CategorieForm
from food.models import Food, Group
from .models import Recipe, Categorie


@login_required
def create_recipe(request):
    if request.method == 'POST':
        if request.POST['identifiant'] == 'recipe':
            form = RecipeForm(request.POST)
            if form.is_valid():
                new_recipe = form.save()
                print(new_recipe.name)
                return redirect(reverse('planning:new_recipe'))
        else:
            form = CategorieForm(request.POST)
            if form.is_valid():
                new_recipe = form.save()
                print(new_recipe.name)
                return redirect(reverse('planning:new_recipe'))

    else:
        form_recipe = RecipeForm()
        form_categorie = CategorieForm()
        context = {
            'form_recipe': form_recipe,
            'form_categ': form_categorie
        }
        return render(request, 'planning/new_recipe.html', context)


@login_required
def show_and_update_db(request):
    foods = Food.objects.all()
    food_group = Group.objects.all()
    recipes = Recipe.objects.all()
    recipe_categ = Categorie.objects.all()

    context = {
        'food': foods,
        'food_group': food_group,
        'recipe': recipes,
        'recipe_categ': recipe_categ
    }

    return render(request, 'planning/databases.html', context)