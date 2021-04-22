from ..models import FoodAndQuantity
from food.models import Food


def create_recipe_with_template(recipe_template, recipe_duplicated):
    """
    Create a new recipe based on a recipe template. (Duplication)
    
    Return state opération.
    
    recipe_template -> instance of <Recipe> object. (recipe exist)
    recipe_duplicated -> instance of  <Recipe> object but not save. (new recipe)
    """
    r_t = recipe_template
    r_d = recipe_duplicated

    r_d.name = r_t.name + ' COPIE'
    r_d.preparation_time = r_t.preparation_time
    r_d.cooking_time = r_t.cooking_time
    r_d.step = r_t.step
    r_d.tip = r_t.tip
    r_d.portion = r_t.portion
    r_d.point = r_t.point
    r_d.typical_recipe_city = r_t.typical_recipe_city
    r_d.source = r_t.source
    r_d.image = r_t.image
    r_d.origin = r_t.origin
    r_d.price_scale = r_t.price_scale
    r_d.level = r_t.level
    r_d.save()

    r_d.utensils.set(r_t.utensils.all())
    r_d.season.set(r_t.season.all())
    r_d.dietary_plan.set(r_t.dietary_plan.all())
    r_d.categories.set(r_t.categories.all())

    food_and_quant = set()
    for f_q in r_t.foodandquantity_set.all():
        new_f_q = FoodAndQuantity()
        new_f_q.recipe = r_d
        new_f_q.food = f_q.food
        new_f_q.recipe_quantity = f_q.recipe_quantity
        new_f_q.recipe_unity = f_q.recipe_unity
        new_f_q.food_purchase_quantity = f_q.food_purchase_quantity
        new_f_q.food_purchase_unity = f_q.food_purchase_unity
        new_f_q.save()
        food_and_quant.add(new_f_q)

    r_d.foodandquantity_set.set(food_and_quant)

    r_d.save()

    return 'ok'