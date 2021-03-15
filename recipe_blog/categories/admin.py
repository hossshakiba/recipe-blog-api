from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)