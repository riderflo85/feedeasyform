from .models import MealsPerDay, Recipe, DayMealsPerDay


def parse_data_new_planning(request_data):
    """
    Parsed the request string data to the python object for create new planning.
    """
    recipes_by_days = []
    index = 0

    for key, value in request_data.items():
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
                    pk=int(x.split('-')[1])
                ) for x in data_splited[1].split('_')[1:]
            ]
            recipes_by_days[index][key][mlp] = recipes
        index += 1

    return recipes_by_days


# {
#     "lundi": "?&lundi-1=_recipeNumber-1_recipeNumber-2&lundi-2=_recipeNumber-3&lundi-3=_recipeNumber-2_recipeNumber-3&lundi-4=_recipeNumber-1_recipeNumber-2&lundi-5=_recipeNumber-1_recipeNumber-2_recipeNumber-3",
#     "mardi": "?&mardi-1=_recipeNumber-1&mardi-2=_recipeNumber-1_recipeNumber-3&mardi-3=_recipeNumber-2&mardi-4=_recipeNumber-3&mardi-5=_recipeNumber-1_recipeNumber-2_recipeNumber-3",
#     "mercredi": "?&mercredi-1=_recipeNumber-1&mercredi-2=_recipeNumber-2_recipeNumber-3&mercredi-3=_recipeNumber-1_recipeNumber-2&mercredi-4=_recipeNumber-3_recipeNumber-2_recipeNumber-1&mercredi-5=_recipeNumber-1_recipeNumber-3",
#     "jeudi": "?&jeudi-1=_recipeNumber-2_recipeNumber-3&jeudi-2=_recipeNumber-1&jeudi-3=_recipeNumber-2&jeudi-4=_recipeNumber-3&jeudi-5=_recipeNumber-1",
#     "vendredi": "?&vendredi-1=_recipeNumber-2&vendredi-2=_recipeNumber-2&vendredi-3=_recipeNumber-3&vendredi-4=_recipeNumber-3&vendredi-5=_recipeNumber-1",
#     "samedi": "?&samedi-1=_recipeNumber-2_recipeNumber-3&samedi-2=_recipeNumber-1_recipeNumber-3&samedi-3=_recipeNumber-2&samedi-4=_recipeNumber-1_recipeNumber-2_recipeNumber-3&samedi-5=_recipeNumber-1_recipeNumber-3",
#     "dimanche": "?&dimanche-1=_recipeNumber-1_recipeNumber-2&dimanche-2=_recipeNumber-1_recipeNumber-2&dimanche-3=_recipeNumber-1_recipeNumber-2&dimanche-4=_recipeNumber-3&dimanche-5=_recipeNumber-2"
# }


def create_new_planning(parsed_data):
    """
    Create the new planning with the parsed data.
    """
    day_instances = []

    for day in parsed_data:
        new_day_mlp_objects = DayMealsPerDay()
        mlps = set()
        for k, v in day.items():
            mlps.add(k)