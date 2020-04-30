from .models import Food, Group


def list_all_food():
    foods = []

    for food in Food.objects.all():
        foods.append((food.pk, food.name))

    return foods

def list_all_group():
    groups = []

    for group in Group.objects.all():
        groups.append((group.pk, group.name))

    return groups
