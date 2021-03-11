from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required

from .models import Planning, MealsPerDay
from .forms import PlanningForm
from recipe.models import CategorieRecipe, DietaryPlan, OriginRecipe, Recipe, Season


@login_required
def create_planning(request):
    if request.method == 'POST':
        form = PlanningForm(request.POST)
        if form.is_valid():
            new_planning = form.save()
            return JsonResponse({'success': True})
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
def search_recipe_by_text(request):
    text_user = request.GET
    print(text_user)

    return JsonResponse({'recipes': 'ok'})


class PlanningDetailView(DetailView):
    model = Planning
    template_name = "recipe/detail.html"
