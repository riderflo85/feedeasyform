import json

from ..models import Planning


def parse_day_recipe(day_instance):
    """
    Get and parse all recipe planning per day.
    """
    mlps = {"fr_name_day": day_instance.name}

    for day in day_instance.daymealsperday_set.all():
        name_mlp = day.meal_per_day.name
        mlps[name_mlp] = [r.name for r in day.recipes.all()]

    return mlps


def parse_planning_data():
    """
    Parse planning data for a json file.
    """
    data = {"plannings": []}

    for planning in Planning.objects.all():
        planning_data = {
            "name": planning.name,
            "premium": planning.premium,
            "season": planning.season.name,
            "origin": planning.origin.name,
            "dietary_plan": planning.dietary_plan.name,
            "monday": parse_day_recipe(planning.monday),
            "tuesday": parse_day_recipe(planning.tuesday),
            "wednesday": parse_day_recipe(planning.wednesday),
            "thursday": parse_day_recipe(planning.thursday),
            "friday": parse_day_recipe(planning.friday),
            "saturday": parse_day_recipe(planning.saturday),
            "sunday": parse_day_recipe(planning.sunday),
        }
        data['plannings'].append(planning_data)

    return data


def generate_json_file(data):
    """
    Generate a json file with all planning.
    Return json file path.
    """
    json_file_name = 'backup_plannings.json'
    with open(json_file_name, 'w') as jsonfile:
        json.dump(
            data, jsonfile, indent=4, ensure_ascii=False
        )
    return json_file_name
