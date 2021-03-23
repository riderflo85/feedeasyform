from django.urls import path
from . import views


app_name = "planning"
urlpatterns = [
    path(
        'detail/planning/<int:pk>',
        views.PlanningDetailView.as_view(),
        name="detail_planning"
    ),
    path('new_planning/', views.create_planning, name="new_planning"),
    path('search/', views.search_recipe_by_text, name="search_recipe"),
    path('filter/', views.search_recipe_by_filter, name="filter_recipe"),
    path('updated/', views.update_planning, name="update_planning"),
]
