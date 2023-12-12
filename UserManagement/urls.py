from django.contrib import admin
from django.urls import path, include
from UserManagement import views

urlpatterns = [
    path("", views.register, name="register"),
    path("register/", views.register, name="register"),
    path("blogs/", views.user, name="user"),
    path("login/", views.login_page, name="login_page"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_page, name="logout_page"),
    path('froala_editor/', include('froala_editor.urls')),
    path('add-blog/',  views.add_blog, name="add_blog"),
    path('blog-detail/<slug>', views.blog_detail, name='blog_detail'),
    path('my-blogs/', views.myblogs, name='myblogs'),
    path('blog-delete/<id>', views.blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', views.blog_update, name="blog_update"),
    path('mental-health/', views.mental_health, name='mental_health'),
    path('heart-disease/', views.heart_disease, name='heart_disease'),
    path('covid19/', views.covid19, name='covid19'),
    path('immunization/', views.immunization, name='immunization')

]
