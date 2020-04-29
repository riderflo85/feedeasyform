from django.urls import path
from . import views


app_name = "food"
urlpatterns = [
    path('new_food', views.create_food, name="new_food"),
]

