from django.contrib import admin
from . import models


@admin.register(models.Tip)
class TipAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "champion",
        "recommand",
    )

    fieldset = (
        (
            None,
            {
                "fields": (
                    "user",
                    "champion",
                    "recommand",
                    "description",
                ),
            },
        ),
    )
