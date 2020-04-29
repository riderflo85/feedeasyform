from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

app_name = "user"
urlpatterns = [
    path(
        '',
        auth_views.LoginView.as_view(
            template_name='user/login.html',
            authentication_form=LoginForm
        ),
        name="login"
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='user/login.html'),
        name="logout"
    ),
    path('task', views.task, name='task'),
]
