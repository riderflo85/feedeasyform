from django.http import JsonResponse, FileResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required

from .forms import RecipeForm, CategorieRecipeForm, UtensilForm, \
    DeleteRecipeForm, DeleteCategForm, DeleteUtensilForm, OriginRecipeForm, \
    DeleteOriginRecipe, DietaryPlanForm, DeleteDietForm
from .models import Level, PriceScale, Recipe, CategorieRecipe, Utensil, OriginRecipe, \
    DietaryPlan, Season
from .utils.complet_new_recipe import complet_recipe_with_foods_and_utensils,\
    parse_foods_and_utensils, added_season_and_diet, parse_diets_and_seasons, \
        updated_recipe_foods_and_utensils, updated_season_and_diet
from .utils.backup_db import generate_zip_file
from .list_all_db import list_all_diet, list_all_season
from food.models import Food, FoodGroup
from food.forms import DeleteFoodForm, DeleteFoodGroupForm


@login_required
def create_recipe(request):
    if request.method == 'POST':
        if request.POST['identifiant'] == 'recipe':
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                new_recipe = form.save()
                foods, utensils = parse_foods_and_utensils(
                    request.POST['foods'],
                    request.POST['utensils'],
                )
                diets, seasons = parse_diets_and_seasons(
                    request.POST['dietary_plan'],
                    request.POST['season']
                )
                complet_recipe_with_foods_and_utensils(
                    new_recipe,
                    foods,
                    utensils
                )
                added_season_and_diet(new_recipe, diets, seasons)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': form.errors})
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
        elif request.POST['identifiant'] == 'diet':
            form = DietaryPlanForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('planning:new_recipe'))

    else:
        form_recipe = RecipeForm()
        form_categorie = CategorieRecipeForm()
        form_utensil = UtensilForm()
        form_origin_recipe = OriginRecipeForm()
        form_diet = DietaryPlanForm()
        form_recipe_diet_field = {
            'label': "Régime alimentaire de la recette",
            'diets': list_all_diet()
        }
        form_recipe_season_field = {
            'label': "Saison de la recette",
            'seasons': list_all_season()
        }
        context = {
            'form_recipe': form_recipe,
            'form_categ': form_categorie,
            'form_uten': form_utensil,
            'form_diet': form_diet,
            'foods': Food.objects.all(),
            'utensils': Utensil.objects.all(),
            'form_origin_recipe': form_origin_recipe,
            'diet_field': form_recipe_diet_field,
            'season_field': form_recipe_season_field
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

        elif request.POST['identifiant'] == 'origin_recipe':
            form = DeleteOriginRecipe(request.POST)
            if form.is_valid():
                origin = form.cleaned_data['origin']
                OriginRecipe.objects.get(pk=int(origin)).delete()

        elif request.POST['identifiant'] == 'diet':
            form = DeleteDietForm(request.POST)
            if form.is_valid():
                diet = form.cleaned_data['diet']
                DietaryPlan.objects.get(pk=int(diet)).delete()

        return redirect(reverse('planning:databases'))

    else:
        foods = Food.objects.order_by('name')
        food_group = FoodGroup.objects.order_by('name')
        recipes = Recipe.objects.order_by('name')
        recipe_categ = CategorieRecipe.objects.order_by('name')
        utensils = Utensil.objects.order_by('name')
        origin_recipes = OriginRecipe.objects.order_by('name')
        dietarys_plan = DietaryPlan.objects.order_by('name')
        form_del_food = DeleteFoodForm()
        form_del_group = DeleteFoodGroupForm()
        form_del_recipe = DeleteRecipeForm()
        form_del_categ = DeleteCategForm()
        form_del_utensil = DeleteUtensilForm()
        form_del_origin = DeleteOriginRecipe()
        form_del_diet = DeleteDietForm()

        context = {
            'foods': foods,
            'food_group': food_group,
            'recipes': recipes,
            'recipe_categ': recipe_categ,
            'utensils': utensils,
            'origin_recipes': origin_recipes,
            'diets': dietarys_plan,
            'del_food': form_del_food,
            'del_group': form_del_group,
            'del_recipe': form_del_recipe,
            'del_categ': form_del_categ,
            'del_utensil': form_del_utensil,
            'del_origin': form_del_origin,
            'del_diet': form_del_diet
        }

        return render(request, 'planning/databases.html', context)

@login_required
def download_json_backup(request):
    file_name = generate_zip_file()
    return FileResponse(
        open(file_name, 'rb'),
        as_attachment=True,
        content_type="application/zip"
    )

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "planning/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categs'] = CategorieRecipe.objects.all()
        context['foods'] = Food.objects.all()
        context['utensils'] = Utensil.objects.all()
        context['price_scale'] = PriceScale.objects.all()
        context['levels'] = Level.objects.all()
        context['origins'] = OriginRecipe.objects.all()
        context['diets'] = DietaryPlan.objects.all()
        context['seasons'] = Season.objects.all()

        return context

    def post(self, *args, **kwargs):
        recipe = Recipe.objects.get(pk=kwargs['pk'])
        request = self.request

        if request.POST.get('postType') != None:
            if request.POST['postType'] == 'update image':
                print(request.POST, request.FILES)
                recipe.image = request.FILES['image']
                recipe.save()
                return JsonResponse({'status': 'done'})

            else:
                return JsonResponse({'status': 'error'})

        else:
            recipe.name = request.POST['name']
            recipe.preparation_time = request.POST['prepTime']
            recipe.cooking_time = request.POST['cookTime']
            recipe.step = request.POST['steps']
            recipe.tip = request.POST['tips']
            recipe.point = request.POST['point']
            recipe.portion = request.POST['portion']
            recipe.typical_recipe_city = request.POST['typical']
            recipe.source = request.POST['source']
            recipe.categorie = CategorieRecipe.objects.get(
                pk=int(request.POST['categ'])
            )
            recipe.price_scale = PriceScale.objects.get(
                pk=int(request.POST['price'])
            )
            recipe.level = Level.objects.get(
                pk=int(request.POST['level'])
            )
            recipe.origin = OriginRecipe.objects.get(
                pk=int(request.POST['origin'])
            )
            recipe.save()

            foods, utensils = parse_foods_and_utensils(
                request.POST['foods'],
                request.POST['utensils'],
            )
            diets, seasons = parse_diets_and_seasons(
                request.POST['dietary_plan'],
                request.POST['season']
            )
            updated_recipe_foods_and_utensils(recipe, foods, utensils)
            updated_season_and_diet(recipe, diets, seasons)

            return JsonResponse({'test': 'ok'})


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


class DietDetailView(DetailView):
    model = DietaryPlan
    template_name = "planning/detail.html"
