from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "product",
        "rating",
    )

    fieldset = (
        (
            None,
            {
                "fields": (
                    "name",
                    "product",
                    "rating",
                    "description",
                    "photo",
                ),
            },
        ),
    )