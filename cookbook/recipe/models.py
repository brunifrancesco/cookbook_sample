from django.db import models

class Recipe(models.Model):
    name = models.TextField(default="", blank=False)
    ingredients = models.TextField(default="", blank=False)
    method = models.TextField(default="", blank=False)