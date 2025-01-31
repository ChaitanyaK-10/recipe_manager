"""
URL configuration for recipe_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # Ensure 'path' is imported
from recipes import views  # Import views from the recipes app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page to list all recipes
    path('add/', views.add_recipe, name='add_recipe'),  # Add new recipe
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),  # Recipe details
    path('recipe/<int:pk>/edit/', views.edit_recipe, name='edit_recipe'),  # Edit recipe
    path('recipe/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),  # Delete recipe
]

