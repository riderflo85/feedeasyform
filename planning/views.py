from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, CategorieForm, UtensilForm
from food.models import Food, Group
from .models import Recipe, Categorie, Utensil


@login_required
def create_recipe(request):
    if request.method == 'POST':
        if request.POST['identifiant'] == 'recipe':
            form = RecipeForm(request.POST)
            if form.is_valid():
                new_recipe = form.save()
                print(new_recipe.name)
                return redirect(reverse('planning:new_recipe'))
        elif request.POST['identifiant'] == 'categorie':
            form = CategorieForm(request.POST)
            if form.is_valid():
                new_recipe = form.save()
                print(new_recipe.name)
                return redirect(reverse('planning:new_recipe'))
        elif request.POST['identifiant'] == 'utensil':
            form = UtensilForm(request.POST)
            if form.is_valid():
                new_utensil = form.save()
                print(new_utensil.name)
                return redirect(reverse('planning:new_recipe'))

    else:
        form_recipe = RecipeForm()
        form_categorie = CategorieForm()
        form_utensil = UtensilForm()
        context = {
            'form_recipe': form_recipe,
            'form_categ': form_categorie,
            'form_uten': form_utensil
        }
        return render(request, 'planning/new_recipe.html', context)


@login_required
def show_and_update_db(request):
    foods = Food.objects.all()
    food_group = Group.objects.all()
    recipes = Recipe.objects.all()
    recipe_categ = Categorie.objects.all()
    utensils = Utensil.objects.all()

    context = {
        'food': foods,
        'food_group': food_group,
        'recipe': recipes,
        'recipe_categ': recipe_categ,
        'utensils': utensils
    }

    return render(request, 'planning/databases.html', context)
