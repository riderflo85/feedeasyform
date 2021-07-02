from django.http.response import JsonResponse
from django.shortcuts import render, redirect, resolve_url, reverse
from django.contrib.auth.decorators import login_required

from .forms import FoodForm, FoodGroupForm, StoreRackForm
from .models import Food, FoodGroup, StoreRack


@login_required
def create_food(request):
    if request.method == 'POST':
        if request.POST['identifiant'] == 'food':
            form = FoodForm(request.POST)
            if form.is_valid():
                new_food = form.save()
                print(new_food.name)
                return redirect(reverse('food:new_food'))
        else:
            form = FoodGroupForm(request.POST)
            if form.is_valid():
                new_group = form.save()
                print(new_group.name)
                return redirect(reverse('food:new_food'))

    else:
        form_food = FoodForm()
        form_group = FoodGroupForm()
        context = {
            'form_food': form_food,
            'form_group': form_group
        }
        return render(request, 'food/new_food.html', context)


@login_required
def set_unit_with_food_group(request):
    if request.method == 'POST':
        metric_unit, imperial_unit = request.POST['unit'].split(';')
        food_group = FoodGroup.objects.get(pk=int(request.POST['id']))

        for food in food_group.food_set.all():
            food.metric_unit = metric_unit.split(':')[1]
            food.imperial_unit = imperial_unit.split(':')[1]
            food.save()

        return JsonResponse({'status': 'ok'})

    else:
        return JsonResponse({'error': 'http method not accepeted'})


@login_required
def update_food_unit(request):
    if request.method == 'POST':
        metric_unit, imperial_unit = request.POST['unit'].split(';')
        food = Food.objects.get(
            pk=int(request.POST['id'])
        )
        food.metric_unit = metric_unit.split(':')[1]
        food.imperial_unit = imperial_unit.split(':')[1]
        food.save()

        return JsonResponse({'status': 'ok'})

    else:
        return JsonResponse({'error': 'http method not accepeted'})


@login_required
def store_rack(request):
    context = {
        'rack_form': StoreRackForm()
    }
    if request.method == 'POST':
        if request.POST.get('postType'):
            st_rack = StoreRack.objects.get(pk=int(request.POST['idRack']))
            if request.POST['postType'] == 'add':
                for fg_id in eval(request.POST['idFoodGroup']):
                    fg = FoodGroup.objects.get(pk=fg_id)
                    fg.store_rack = st_rack
                    fg.save()
            elif request.POST['postType'] == 'delete':
                for fg_id in eval(request.POST['idFoodGroup']):
                    fg = FoodGroup.objects.get(pk=fg_id)
                    st_rack.foodgroup_set.remove(fg)
            return JsonResponse({"state": "done"})
        else:
            form = StoreRackForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse("food:store_rack"))
            else:
                context['rack_form'] = form
            return render(request, 'food/new_rack.html', context)

    else:
        return render(request, 'food/new_rack.html', context)