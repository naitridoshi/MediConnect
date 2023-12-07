from django.contrib import admin
from django.urls import path, include
from UserManagement import views

urlpatterns = [
    path("", views.register, name="register")
]
