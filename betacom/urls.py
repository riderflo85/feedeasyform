from django.urls import path
from . import views


app_name = "beta"
urlpatterns = [
    path('', views.register_beta, name="register_beta"),
]
