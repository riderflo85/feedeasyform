from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, CategorieForm, UtensilForm, FoodQuantityForm, \
    DeleteRecipeForm, DeleteCategForm, DeleteUtensilForm
from .models import Recipe, Categorie, Utensil
from food.models import Food, Group
from food.forms import DeleteFoodForm, DeleteGroupForm


@login_required
def create_recipe(request):
    if request.method == 'POST':
        if request.POST['identifiant'] == 'recipe':
            form = RecipeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('planning:new_recipe'))
        elif request.POST['identifiant'] == 'categorie':
            form = CategorieForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('planning:new_recipe'))
        elif request.POST['identifiant'] == 'utensil':
            form = UtensilForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('planning:new_recipe'))
        elif request.POST['identifiant'] == 'food_quantity':
            form = FoodQuantityForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('planning:new_recipe'))

    else:
        form_recipe = RecipeForm()
        form_categorie = CategorieForm()
        form_utensil = UtensilForm()
        form_food_quantity = FoodQuantityForm()
        context = {
            'form_recipe': form_recipe,
            'form_categ': form_categorie,
            'form_uten': form_utensil,
            'form_food_quantity': form_food_quantity,
        }
        return render(request, 'planning/new_recipe.html', context)


@login_required
def show_and_update_db(request):
    if request.method == 'POST':
        if request.POST['identifiant'] == 'recipe':
            form = DeleteRecipeForm(request.POST)
            if form.is_valid():
                recipe = form.cleaned_data['recipe']
                Recipe.objects.get(pk=int(recipe)).delete()
    
        elif request.POST['identifiant'] == 'categ':
            form = DeleteCategForm(request.POST)
            if form.is_valid():
                categ = form.cleaned_data['categ']
                Categorie.objects.get(pk=int(categ)).delete()
        
        elif request.POST['identifiant'] == 'utensil':
            form = DeleteUtensilForm(request.POST)
            if form.is_valid():
                utensil = form.cleaned_data['utensil']
                Utensil.objects.get(pk=int(utensil)).delete()

        elif request.POST['identifiant'] == 'food':
            form = DeleteFoodForm(request.POST)
            if form.is_valid():
                food = form.cleaned_data['food']
                Food.objects.get(pk=int(food)).delete()

        elif request.POST['identifiant'] == 'group':
            form = DeleteGroupForm(request.POST)
            if form.is_valid():
                group = form.cleaned_data['group']
                Group.objects.get(pk=int(group)).delete()
        
        return redirect(reverse('planning:databases'))

    else:
        foods = Food.objects.all()
        food_group = Group.objects.all()
        recipes = Recipe.objects.all()
        recipe_categ = Categorie.objects.all()
        utensils = Utensil.objects.all()
        form_del_food = DeleteFoodForm()
        form_del_group = DeleteGroupForm()
        form_del_recipe = DeleteRecipeForm()
        form_del_categ = DeleteCategForm()
        form_del_utensil = DeleteUtensilForm()

        context = {
            'foods': foods,
            'food_group': food_group,
            'recipes': recipes,
            'recipe_categ': recipe_categ,
            'utensils': utensils,
            'del_food': form_del_food,
            'del_group': form_del_group,
            'del_recipe': form_del_recipe,
            'del_categ': form_del_categ,
            'del_utensil': form_del_utensil
        }

        return render(request, 'planning/databases.html', context)
