from ..models import MealsPerDay, Recipe, DayMealsPerDay, Day, Planning
from recipe.models import Season, OriginRecipe, DietaryPlan


def parse_data_new_planning(request_data):
    """
    Parsed the request string data to the python object for create new planning.
    """
    recipes_by_days = []
    index = 0
    data = dict(request_data)
    data.pop('name')
    data.pop('season')
    data.pop('origin')
    data.pop('dietary_plan')
    data.pop('premium')

    for key, value in data.items():
        mlp_and_recipes = value[0].split('?&')[1].split('&')
        recipes_by_days.append({key: {}})
        for mlp_recipe in mlp_and_recipes:
            data_splited = mlp_recipe.split('=')
            mlp = MealsPerDay.objects.get(
                pk=int(data_splited[0].split('-')[1])
            )
            # Get a recipe ID in the data string request send by the user
            recipes = [
                Recipe.objects.get(
                    pk=int(x.split('-')[1])
                ) for x in data_splited[1].split('_')[1:]
            ]
            recipes_by_days[index][key][mlp] = recipes
        index += 1

    return recipes_by_days


# {"lundi": "?&lundi-1=_recipeNumber-1_recipeNumber-2&lundi-2=_recipeNumber-3&lundi-3=_recipeNumber-2_recipeNumber-3&lundi-4=_recipeNumber-1_recipeNumber-2&lundi-5=_recipeNumber-1_recipeNumber-2_recipeNumber-3","mardi": "?&mardi-1=_recipeNumber-1&mardi-2=_recipeNumber-1_recipeNumber-3&mardi-3=_recipeNumber-2&mardi-4=_recipeNumber-3&mardi-5=_recipeNumber-1_recipeNumber-2_recipeNumber-3","mercredi": "?&mercredi-1=_recipeNumber-1&mercredi-2=_recipeNumber-2_recipeNumber-3&mercredi-3=_recipeNumber-1_recipeNumber-2&mercredi-4=_recipeNumber-3_recipeNumber-2_recipeNumber-1&mercredi-5=_recipeNumber-1_recipeNumber-3","jeudi": "?&jeudi-1=_recipeNumber-2_recipeNumber-3&jeudi-2=_recipeNumber-1&jeudi-3=_recipeNumber-2&jeudi-4=_recipeNumber-3&jeudi-5=_recipeNumber-1","vendredi": "?&vendredi-1=_recipeNumber-2&vendredi-2=_recipeNumber-2&vendredi-3=_recipeNumber-3&vendredi-4=_recipeNumber-3&vendredi-5=_recipeNumber-1","samedi": "?&samedi-1=_recipeNumber-2_recipeNumber-3&samedi-2=_recipeNumber-1_recipeNumber-3&samedi-3=_recipeNumber-2&samedi-4=_recipeNumber-1_recipeNumber-2_recipeNumber-3&samedi-5=_recipeNumber-1_recipeNumber-3","dimanche": "?&dimanche-1=_recipeNumber-1_recipeNumber-2&dimanche-2=_recipeNumber-1_recipeNumber-2&dimanche-3=_recipeNumber-1_recipeNumber-2&dimanche-4=_recipeNumber-3&dimanche-5=_recipeNumber-2","name":"planning hiver"}


def create_new_planning(parsed_recipes, planning_other_data):
    """
    Create the new planning with the parsed data.
    """
    day_instances = []
    is_good = False
    p_o_d = planning_other_data

    for day in parsed_recipes:
        for k, v in day.items():
            new_day = Day()
            new_day.name = k
            new_day.save()
            for mlp, recipes in v.items():
                new_day_mlp_objects = DayMealsPerDay()
                new_day_mlp_objects.meal_per_day = mlp
                new_day_mlp_objects.day = new_day
                new_day_mlp_objects.save()
                new_day_mlp_objects.recipes.set(recipes)
            day_instances.append(new_day)

    new_planning = Planning()
    try:
        new_planning.name = p_o_d['name']
        new_planning.premium = bool(p_o_d['premium'])
        new_planning.season = Season.objects.get(pk=p_o_d['season'])
        new_planning.origin = OriginRecipe.objects.get(pk=p_o_d['origin'])
        new_planning.dietary_plan = DietaryPlan.objects.get(pk=p_o_d['diet'])
        new_planning.monday = day_instances[0]
        new_planning.tuesday = day_instances[1]
        new_planning.wednesday = day_instances[2]
        new_planning.thursday = day_instances[3]
        new_planning.friday = day_instances[4]
        new_planning.saturday = day_instances[5]
        new_planning.sunday = day_instances[6]
        new_planning.save()
        is_good = True
    except:
        is_good = False

    return is_good


def parse_recipes_update_planning(request_data):
    """
    Parsed the request string data to the python object for updated a planning.
    """
    recipes_by_days = []
    skip_keys = ["name", "id", "season", "origin", "diet", "premium"]
    index = 0

    for key, value in request_data.items():
        if key not in skip_keys:
            mlp_and_recipes = value.split('?&')[1].split('&')
            recipes_by_days.append({key: {}})
            for mlp_recipe in mlp_and_recipes:
                data_splited = mlp_recipe.split('=')
                mlp = MealsPerDay.objects.get(
                    pk=int(data_splited[0].split('-')[1])
                )
                # Get a recipe ID in the data string request send by the user
                recipes = [
                    Recipe.objects.get(
                        pk=int(x)
                    ) for x in data_splited[1].split('_')[1:]
                ]
                recipes_by_days[index][key][mlp] = recipes
            index += 1

    return recipes_by_days


def update_planning_data(planning_instance, new_recipes, new_data):
    """
    Update the recipes in the day in a planning instance and many informaitons.
    """
    day_instances = []
    is_good = False

    for day in new_recipes:
        for k, v  in day.items():
            day_name, day_id = k.split('-')
            day = Day.objects.get(pk=int(day_id))
            if day.name == day_name:
                for mlp, recipes in v.items():
                    day_mlp_object = DayMealsPerDay.objects.filter(
                        day=day
                    ).filter(meal_per_day=mlp)[0]
                    day_mlp_object.recipes.set(recipes)
                    day_mlp_object.save()
            day.save()
            day_instances.append(day)

    try:
        planning_instance.monday = day_instances[0]
        planning_instance.tuesday = day_instances[1]
        planning_instance.wednesday = day_instances[2]
        planning_instance.thursday = day_instances[3]
        planning_instance.friday = day_instances[4]
        planning_instance.saturday = day_instances[5]
        planning_instance.sunday = day_instances[6]
        planning_instance.name = new_data['name']
        planning_instance.season = new_data['season']
        planning_instance.origin = new_data['origin']
        planning_instance.dietary_plan = new_data['diet']
        if new_data['is_premium'] == 'true':
            planning_instance.premium = True
        elif new_data['is_premium'] == 'false':
            planning_instance.premium = False
        planning_instance.save()
        is_good = True
    except:
        is_good = False
    
    return is_good