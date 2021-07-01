from .models import Food, FoodGroup, StoreRack


def list_all_food():
    foods = []

    for food in Food.objects.all():
        foods.append((food.pk, food.name))

    return foods

def list_all_group():
    groups = []

    for group in FoodGroup.objects.all():
        groups.append((group.pk, group.name))

    return groups

def list_all_racks():
    store_racks = []

    for sr in StoreRack.objects.all():
        store_racks.append((sr.pk, sr.name))

    return store_racks
