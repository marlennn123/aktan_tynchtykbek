from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ('email',)
    username = None
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ["is_staff"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        (
            "Other info",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "is_active",
                    "is_staff",
                ],
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",

                    "is_active",
                    "is_staff",
                ]
            },
        ),
    ]