from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#    return HttpResponse("hello workd")

# def index(request):
#     return HttpResponse("<html><body><b>Hello, <b/> world<body></hml>")
from recipe.models import Recipe


def index(request):
    current_date = datetime.now()
    recipes = Recipe.objects.all()
    return render(request, "index.html", context={"current_date": current_date, "recipes":recipes})