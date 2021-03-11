def recipe_serializer(all_recipes):
    data = []
    for recipe in all_recipes:
        data.append({
            'id': recipe.pk,
            'name': recipe.name,
            'categ': recipe.categorie.name,
            'seasons': [x.name for x in recipe.season.all()],
            'diets': [x.name for x in recipe.dietary_plan.all()],
            'image': recipe.image.url
        })
    return data