from django.urls import path
from . import views


app_name = "planning"
urlpatterns = [
     path('new_recipe/', views.create_recipe, name='new_recipe'),
     path('databases/', views.show_and_update_db, name='databases'),
     path('detail/recipe/<int:pk>/',
          views.RecipeDetailView.as_view(), name="detailrecipe"),
     path('detail/utensil/<int:pk>/',
          views.UtensilDetailView.as_view(), name="detailutensil"),
     path('detail/categorie/<int:pk>/',
          views.CategorieDetailView.as_view(), name="detailcategorie"),
     path('detail/food/<int:pk>/',
          views.FoodDetailView.as_view(), name="detailfood"),
     path('detail/group/<int:pk>/',
          views.GroupDetailView.as_view(), name="detailgroup"),
     path('detail/origin/<int:pk>/',
          views.OriginRecipeDetailView.as_view(), name="detailorigin"),
]
