from django.urls import path
from . import views


app_name = "food"
urlpatterns = [
    path('new_food/', views.create_food, name="new_food"),
    path('set_food_group_unit/', views.set_unit_with_food_group, name="set_unit"),
    path('update_food_unit/', views.update_food_unit, name="update_food_unit")
]

