from planning.models import Food, FoodAndQuantity, Utensil, Season, DietaryPlan


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


def parse_diets_and_seasons(diets, seasons):
    """
    Parsed the diets and seasons for the new recipe.
    diets -> str : '?&d=id&d=id...'
    seasons -> str : '?&s=id&s=id...'

    return diets -> list : [id, ...]
    return seasons -> list : [id, ...]
    """
    parsed_diets = diets.replace('?&d=', '').split('&d=')
    parsed_seasons = seasons.replace('?&s=', '').split('&s=')

    return parsed_diets, parsed_seasons


def complet_recipe_with_foods_and_utensils(instance_recipe, foods, utensils):
    """
    Add the foods and utensils in the new recipe.
    instance_recipe -> <class 'planning.models.Recipe'>
    foods -> list : [
        {'id': int, 'quantity': string},
        ...
    ]
    utensils -> list : [id, ...]
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


def added_season_and_diet(instance_recipe, diets, seasons):
    """
    Add the dietary plan and season in the new recipe.
    instance_recipe -> <class 'planning.models.Recipe'>
    diets -> list : [id, ...]
    seasons -> list : [id, ...]
    """

    recipe = instance_recipe
    instance_diets = set()
    instance_seasons = set()

    for diet in diets:
        d = DietaryPlan.objects.get(pk=int(diet))
        instance_diets.add(d)

    for season in seasons:
        s = Season.objects.get(pk=int(season))
        instance_seasons.add(s)

    recipe.dietary_plan.set(instance_diets)
    recipe.season.set(instance_seasons)

    recipe.save()
