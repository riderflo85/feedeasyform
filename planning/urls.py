from django.urls import path
from . import views


app_name = "planning"
urlpatterns = [
    path('new_recipe/', views.create_recipe, name='new_recipe'),
    path('databases/', views.show_and_update_db, name='databases'),
]
