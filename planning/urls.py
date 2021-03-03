from django.urls import path
from . import views


app_name = "planning"
urlpatterns = [
    path(
        'detail/planning/<int:pk>',
        views.PlanningDetailView.as_view(),
        name="detail_planning"
    ),
]
