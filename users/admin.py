from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'surname', 'name', 'middlename', 'email', 'phone']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Пользовательская информация',
            {
                'fields': (
                    'surname',
                    'name',
                    'middlename',
                    'phone',
                    'status'
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Пользовательская информация',
            {
                'fields': (
                    'surname',
                    'name',
                    'middlename',
                    'phone',
                    'status'
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
