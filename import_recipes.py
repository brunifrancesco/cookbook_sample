import requests
from recipe.models import Recipe


data = requests.get("https://raw.githubusercontent.com/raywenderlich/recipes/master/Recipes.json").json()

for recipe in data:
  name = recipe['name']
  ingredients= "\n".join([ "%s of %s" %(ingredient['quantity'], ingredient['name']) for ingredient in recipe['ingredients']])  
  flow = "\n".join(recipe['steps'])
  image_url = recipe['imageURL']
  Recipe(name=name, ingredients=ingredients, method=flow, image_url=image_url).save()  
  
