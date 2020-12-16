from django.views.generic.detail import DetailView
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required

from .forms import RecipeForm, CategorieRecipeForm, UtensilForm, \
    DeleteRecipeForm, DeleteCategForm, DeleteUtensilForm, OriginRecipeForm, \
    DeleteOriginRecipe
from .models import Recipe, CategorieRecipe, Utensil, OriginRecipe
from food.models import Food, FoodGroup
from food.forms import DeleteFoodForm, DeleteFoodGroupForm


@login_required
def create_recipe(request):
    if request.method == 'POST':
        if request.POST['identifiant'] == 'recipe':
            print(request.POST)
            form = RecipeForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                # form.save()
                return redirect(reverse('planning:new_recipe'))
            else:
                print(form.errors)
                # print('in the error form bloc', request.POST)
        elif request.POST['identifiant'] == 'categorie_recipe':
            form = CategorieRecipeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('planning:new_recipe'))
        elif request.POST['identifiant'] == 'utensil':
            form = UtensilForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('planning:new_recipe'))
        elif request.POST['identifiant'] == 'origin_recipe':
            form = OriginRecipeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('planning:new_recipe'))

    else:
        form_recipe = RecipeForm()
        form_categorie = CategorieRecipeForm()
        form_utensil = UtensilForm()
        form_origin_recipe = OriginRecipeForm()
        context = {
            'form_recipe': form_recipe,
            'form_categ': form_categorie,
            'form_uten': form_utensil,
            'foods': Food.objects.all(),
            'utensils': Utensil.objects.all(),
            'form_origin_recipe': form_origin_recipe,
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
                CategorieRecipe.objects.get(pk=int(categ)).delete()
        
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
            form = DeleteFoodGroupForm(request.POST)
            if form.is_valid():
                group = form.cleaned_data['group']
                FoodGroup.objects.get(pk=int(group)).delete()
        
        return redirect(reverse('planning:databases'))

    else:
        foods = Food.objects.all()
        food_group = FoodGroup.objects.all()
        recipes = Recipe.objects.all()
        recipe_categ = CategorieRecipe.objects.all()
        utensils = Utensil.objects.all()
        origin_recipes = OriginRecipe.objects.all()
        form_del_food = DeleteFoodForm()
        form_del_group = DeleteFoodGroupForm()
        form_del_recipe = DeleteRecipeForm()
        form_del_categ = DeleteCategForm()
        form_del_utensil = DeleteUtensilForm()
        form_del_origin = DeleteOriginRecipe()

        context = {
            'foods': foods,
            'food_group': food_group,
            'recipes': recipes,
            'recipe_categ': recipe_categ,
            'utensils': utensils,
            'origin_recipes': origin_recipes,
            'del_food': form_del_food,
            'del_group': form_del_group,
            'del_recipe': form_del_recipe,
            'del_categ': form_del_categ,
            'del_utensil': form_del_utensil,
            'del_origin': form_del_origin
        }

        return render(request, 'planning/databases.html', context)

# @login_required
class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "planning/detail.html"


class CategorieDetailView(DetailView):
    model = CategorieRecipe
    template_name = "planning/detail.html"


class UtensilDetailView(DetailView):
    model = Utensil
    template_name = "planning/detail.html"

class FoodDetailView(DetailView):
    model = Food
    template_name = "planning/detail.html"

class GroupDetailView(DetailView):
    model = FoodGroup
    template_name = "planning/detail.html"

class OriginRecipeDetailView(DetailView):
    model = OriginRecipe
    template_name = "planning/detail.html"
