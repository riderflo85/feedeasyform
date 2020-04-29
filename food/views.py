from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Food, Group
from .forms import FoodForm, GroupForm


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
            form = GroupForm(request.POST)
            if form.is_valid():
                new_group = form.save()
                print(new_group.name)
                return redirect(reverse('food:new_food'))

    else:
        form_food = FoodForm()
        form_group = GroupForm()
        context = {
            'form_food': form_food,
            'form_group': form_group
        }
        return render(request, 'food/new_food.html', context)
