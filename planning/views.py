from django.http import JsonResponse
from django.http.response import FileResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Planning, MealsPerDay
from .forms import PlanningForm
from .serializers import recipe_serializer
from .utils.create_update import (
    parse_data_new_planning,
    create_new_planning,
    parse_data_update_planning,
    update_planning_recipes
)
from .utils import download
from recipe.models import CategorieRecipe, DietaryPlan, OriginRecipe, Recipe, Season


@login_required
def create_planning(request):
    if request.method == 'POST':
        parsed_data = parse_data_new_planning(request.POST)
        other_data = {
            "name": request.POST['name'],
            "season": int(request.POST['season']),
            "origin": int(request.POST['origin']),
            "diet": int(request.POST['dietary_plan']),
            "premium": request.POST['premium']
        }
        state = create_new_planning(parsed_data, other_data)

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
    plannings_parsed = download.parse_planning_data()
    file_path = download.generate_json_file(plannings_parsed)
    return FileResponse(
        open(file_path, 'rb'),
        as_attachment=True,
    )
