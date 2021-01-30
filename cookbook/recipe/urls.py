from django.contrib import admin
from django.urls import path, include

from recipe.views import index, add_recipe, detail

urlpatterns = [
    path('new', add_recipe, name = "new_recipe"),
    path('detail/<int:recipe_id>', detail, name= "detail"),
    path('', index, name="index")
]