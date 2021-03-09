from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_special_member', 'is_staff')
    fieldsets = (
        ('Identical Info', {'fields': ('username', 'email', 'first_name', 'last_name', 'date_joined')}),
        ('Password', {'fields': ('password',)}),
        ('Authorization', {'fields': ('is_special', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ('Identical Info', {'fields': ('username', 'email', 'first_name', 'last_name', 'date_joined')}),
        ('Password', {'fields': ('password1', 'password2')}),
        ('Authorization', {'fields': ('is_special', 'is_staff', 'is_active')}),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'date_joined')


admin.site.register(User, UserAdmin)
