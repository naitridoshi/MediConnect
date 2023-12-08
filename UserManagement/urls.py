from django.contrib import admin
from django.urls import path, include
from UserManagement import views

urlpatterns = [
    path("", views.register, name="register"),
    path("user/", views.user, name="user"),
    path("login/", views.login_page, name="login_page"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_page, name="logout_page"),
]
