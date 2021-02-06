from django.contrib.auth.models import User
from django.db import models

class Recipe(models.Model):
    name = models.TextField(default="", blank=False)
    ingredients = models.TextField(default="", blank=False)
    method = models.TextField(default="", blank=False)
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)