from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from django_advanced.user_app.models import Profile
from django_advanced.user_app.forms import CustomUserCreateForm, CustomUserChangeForm


UserModel = get_user_model()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(UserModel)
class UserAdmin(UserAdmin):
    model = UserModel
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )