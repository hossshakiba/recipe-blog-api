from django.contrib import admin

from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    class Meta:
        model = Recipe

admin.site.register(Recipe, RecipeAdmin)
