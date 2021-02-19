from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# def index(request):
#    return HttpResponse("hello workd")

# def index(request):
#     return HttpResponse("<html><body><b>Hello, <b/> world<body></hml>")
from recipe.forms import NewRecipeForm
from recipe.models import Recipe
from cookbook.celery import  debug_task

@login_required(login_url="/users/login")
def index(request):
    current_date = datetime.now()
    recipes = Recipe.objects.all()
    return render(request, "index.html", context={"current_date": current_date, "recipes":recipes})


@login_required(login_url="/users/login")
def add_recipe(request):
    if request.method == "GET":
        return render(request, "add_recipe.html", context={"form": NewRecipeForm()})
    if request.method == "POST":
        form = NewRecipeForm(request.POST)
        if form.is_valid():
            recipe = Recipe(name=form.cleaned_data['name'], ingredients=form.cleaned_data['ingredients'], method=form.cleaned_data['method'])
            recipe.user = request.user
            recipe.save()
    return render(request, "add_recipe.html", context={"form": form})


@login_required(login_url="/users/login")
def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", context={"recipe": recipe})