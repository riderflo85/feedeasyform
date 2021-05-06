import os, json
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import Planning, MealsPerDay
from .forms import PlanningForm
from .serializers import recipe_serializer
from .utils import (
    parse_data_new_planning,
    create_new_planning,
    parse_data_update_planning,
    update_planning_recipes
)
from recipe.models import CategorieRecipe, DietaryPlan, OriginRecipe, Recipe, Season


@login_required
def create_planning(request):
    if request.method == 'POST':
        parsed_data = parse_data_new_planning(request.POST)
        state = create_new_planning(parsed_data, request.POST['name'])

        return JsonResponse({'success': state})
    else:
        days = [
            {'id': 1, 'name': 'lundi'},
            {'id': 2, 'name': 'mardi'},
            {'id': 3, 'name': 'mercredi'},
            {'id': 4, 'name': 'jeudi'},
            {'id': 5, 'name': 'vendredi'},
            {'id': 6, 'name': 'samedi'},
            {'id': 7, 'name': 'dimanche'},
        ]
        context = {
            'form_planning': PlanningForm(),
            'week': days,
            'meals_per_day': MealsPerDay.objects.all(),
            'recipes': Recipe.objects.all(),
            'categs': CategorieRecipe.objects.order_by('name'),
            'origins': OriginRecipe.objects.order_by('name'),
            'diets': DietaryPlan.objects.order_by('name'),
            'seasons': Season.objects.order_by('name')
        }
        return render(request, 'planning/new_planning.html', context)


@login_required
def update_planning(request):
    if request.method == 'POST':
        planning = Planning.objects.get(pk=int(request.POST['id']))
        parsed_data = parse_data_update_planning(request.POST)
        state = update_planning_recipes(planning, parsed_data)

        return JsonResponse({'status': state})


@login_required
def search_recipe_by_text(request):
    text_user = request.GET['text']

    return JsonResponse({
        'recipes': recipe_serializer(
            Recipe.objects.filter(name__icontains=text_user)
        )
    })


@login_required
def search_recipe_by_filter(request):
    season = request.GET['season']
    origin = request.GET['origin']
    diet = request.GET['diet']
    categ = request.GET['categ']

    if request.GET['text'] != '':
        recipes_done = Recipe.objects.filter(
            name__icontains=request.GET['text']
        )

    else:
        recipes_done = Recipe.objects.all()

    if season != '':
        recipes_done = recipes_done.filter(
            season=Season.objects.get(pk=int(season))
        )
    if origin != '':
        recipes_done = recipes_done.filter(
            origin=int(origin)
        )
    if diet != '':
        recipes_done = recipes_done.filter(
            dietary_plan=DietaryPlan.objects.get(pk=int(diet))
        )
    if categ != '':
        recipes_done = CategorieRecipe.objects.get(
            pk=int(categ)
        ).recipe_set.all()

    return JsonResponse({
        'recipes': recipe_serializer(recipes_done)
    })


class PlanningDetailView(DetailView):
    model = Planning
    template_name = "recipe/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categs'] = CategorieRecipe.objects.order_by('name')
        context['origins'] = OriginRecipe.objects.order_by('name')
        context['diets'] = DietaryPlan.objects.order_by('name')
        context['seasons'] = Season.objects.order_by('name')
        context['recipes'] = Recipe.objects.all()
        context['meals_per_day'] = MealsPerDay.objects.all()

        return context


@login_required
def download_planning(request):
    data = {"plannings": []}

    for planning in Planning.objects.all():
        planning_data = {
            "name": planning.name,
            "mon_pti_dej": [x.name for x in
                planning.monday.daymealsperday_set.filter(
                    meal_per_day=MealsPerDay.objects.get(
                        name="petit déjeuner"
                    )
                )[0].recipes.all()],
            "mon_def": [x.name for x in
                planning.monday.daymealsperday_set.filter(
                    meal_per_day=MealsPerDay.objects.get(
                        name="déjeuner"
                    )
            )[0].recipes.all()],
            "mon_gout": [x.name for x in
                planning.monday.daymealsperday_set.filter(
                    meal_per_day=MealsPerDay.objects.get(
                        name="collation 16h"
                    )
            )[0].recipes.all()],
            "mon_din": planning.monday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="dîner"
                )
            )[0].recipes.all(),
            "tue_pti_dej": planning.tuesday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="petit déjeuner"
                )
            )[0].recipes.all(),
            "tue_def": planning.tuesday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="déjeuner"
                )
            )[0].recipes.all(),
            "tue_gout": planning.tuesday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="collation 16h"
                )
            )[0].recipes.all(),
            "tue_din": planning.tuesday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="dîner"
                )
            )[0].recipes.all(),
            "wed_pti_dej": planning.wednesday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="petit déjeuner"
                )
            )[0].recipes.all(),
            "wed_def": planning.wednesday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="déjeuner"
                )
            )[0].recipes.all(),
            "wed_gout": planning.wednesday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="collation 16h"
                )
            )[0].recipes.all(),
            "wed_din": planning.wednesday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="dîner"
                )
            )[0].recipes.all(),
            "thu_pti_dej": planning.thursday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="petit déjeuner"
                )
            )[0].recipes.all(),
            "thu_def": planning.thursday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="déjeuner"
                )
            )[0].recipes.all(),
            "thu_gout": planning.thursday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="collation 16h"
                )
            )[0].recipes.all(),
            "thu_din": planning.thursday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="dîner"
                )
            )[0].recipes.all(),
            "fri_pti_dej": planning.friday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="petit déjeuner"
                )
            )[0].recipes.all(),
            "fri_def": planning.friday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="déjeuner"
                )
            )[0].recipes.all(),
            "fri_gout": planning.friday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="collation 16h"
                )
            )[0].recipes.all(),
            "fri_din": planning.friday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="dîner"
                )
            )[0].recipes.all(),
            "sat_pti_dej": planning.saturday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="petit déjeuner"
                )
            )[0].recipes.all(),
            "sat_def": planning.saturday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="déjeuner"
                )
            )[0].recipes.all(),
            "sat_gout": planning.saturday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="collation 16h"
                )
            )[0].recipes.all(),
            "sat_din": planning.saturday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="dîner"
                )
            )[0].recipes.all(),
            "sun_pti_dej": planning.sunday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="petit déjeuner"
                )
            )[0].recipes.all(),
            "sun_def": planning.sunday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="déjeuner"
                )
            )[0].recipes.all(),
            "sun_gout": planning.sunday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="collation 16h"
                )
            )[0].recipes.all(),
            "sun_din": planning.sunday.daymealsperday_set.filter(
                meal_per_day=MealsPerDay.objects.get(
                    name="dîner"
                )
            )[0].recipes.all(),
        }
