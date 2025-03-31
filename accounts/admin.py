from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'date_of_birth', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone_number', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)