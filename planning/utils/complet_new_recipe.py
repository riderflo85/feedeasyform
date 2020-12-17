from planning.models import Food, FoodAndQuantity, Utensil


def parse_foods_and_utensils(foods, utensils):
    """
    Parsed the foods and utensils for the new recipe.
    foods -> str : '?&f=id:nameFoods:quantityAndUnity&f=id:nameFoods:...'
    utensils -> str : '?&u=id:name&u=id:name&...'

    return foods -> list : [
        {
            'id_food': '356',
            'name': 'Fruits rouges',
            'quantity': '200 g'
        },
        ...
    ]
    return utensils -> list : [
        {
            'id_utensil': '10',
            'name': 'saladier'
        },
        ...
    ]
    """
    pre_parsed_foods = foods.replace('?&f=', '').split('&f=')
    pre_parsed_utensils = utensils.replace('?&u=', '').split('&u=')
    parsed_foods = []
    parsed_utensils = []

    for food in pre_parsed_foods:
        data = food.split(':')
        parsed_foods.append({
            'id_food': data[0],
            'name': data[1],
            'quantity': data[2]
        })

    for utensil in pre_parsed_utensils:
        data = utensil.split(':')
        parsed_utensils.append({
            'id_utensil': data[0],
            'name': data[1]
        })

    return parsed_foods, parsed_utensils


def complet_recipe_with_foods_and_utensils(instance_recipe, foods, utensils):
    """
    Add the foods and utensils in the new recipe.
    instance_recipe -> <class 'planning.models.Recipe'>
    foods -> str : '?&id:nameFoods:quantityAndUnity&id:nameFoods:...'
    utensils -> str : '?&id:name&id:name&...'
    """
    
    recipe = instance_recipe
    instances_utensil = set()

    for food in foods:
        f = Food.objects.get(pk=int(food['id_food']))
        fq = FoodAndQuantity()
        fq.quantity = food['quantity']
        fq.food = f
        fq.recipe = recipe
        fq.save()

    for utensil in utensils:
        u = Utensil.objects.get(pk=int(utensil['id_utensil']))
        instances_utensil.add(u)

    recipe.utensils.set(instances_utensil)
    recipe.save()
    