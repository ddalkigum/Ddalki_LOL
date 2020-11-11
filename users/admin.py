from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "nickname",
        "email",
        "gender",
        "birthdate",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Basic info",
            {
                "fields": (
                    "bio",
                    "nickname",
                    "gender",
                    "address",
                    "avatar",
                ),
            },
        ),
    )