from django.urls import path
from . import views


app_name = "beta"
urlpatterns = [
    path('', views.index, name="index_beta"),
    path('register', views.register_beta, name="register"),
    path('download', views.download, name="download")
]
