from django.contrib import admin

from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    class Meta:
        model = Ingredient


admin.site.register(Ingredient, IngredientAdmin)