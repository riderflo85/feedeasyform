from django.urls import path
from . import views


app_name = "recipe"
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
     path('detail/diet/<int:pk>/',
          views.DietDetailView.as_view(), name="detaildiet"),
     path('detail/store_rack/<int:pk>/',
          views.StoreRackDetailView.as_view(), name="detailreack"),
     path('backup_database/', views.download_json_backup, name="backup_db"),
     path('update_food_name/', views.update_food_name, name="update_food"),
     path('backup_all_data/', views.download_dumpdata, name="backup_dumpdata"),
     path('download_csv/', views.download_csv_data, name="download_csv"),
     path('duplicate_recipe/', views.duplicate_recipe, name="duplicate_recipe"),
]
