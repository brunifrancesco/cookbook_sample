from django.contrib import admin
from django.utils.html import format_html

from recipe.models import  Recipe

class MainPlateFilter(admin.SimpleListFilter):
    title = "Filtra per piatto"
    parameter_name = 'plate'

    def lookups(self, request, model_admin):
        return [
            ('Pizza', 'Pizza'),
            ('Salad', 'Insalata')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'Pizza':
            return queryset.filter(name__contains='pizza')
        if self.value() == 'Salad':
            return queryset.filter(name__contains='salad')
        return queryset

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cut_ingredients', 'image_url_img')
    list_filter = (MainPlateFilter, )

    def cut_ingredients(self, obj):
        if(len(obj.ingredients) < 50):
            return obj.ingredients
        else:
            return obj.ingredients[0:50] + "..."

    def image_url_img(self, obj):
        return format_html('<img width="40" src="%s" />' %obj.image_url)

    image_url_img.allow_tags = True
admin.site.register(Recipe, RecipeAdmin)