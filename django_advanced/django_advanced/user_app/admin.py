from django.contrib import admin
from django_advanced.user_app.models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
 