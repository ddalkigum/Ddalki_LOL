from django.contrib import admin
from champions import models


@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):

    list_display = ("name",)


@admin.register(models.Line)
class LineAdmin(admin.ModelAdmin):

    list_display = ("name",)


@admin.register(models.Champion)
class ChampionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "title",
    )

    fieldsets = (
        (
            "Basic",
            {
                "fields": (
                    "name",
                    "title",
                    "bio",
                    "square_image",
                    "loading_image",
                ),
            },
        ),
        (
            "In-game",
            {
                "fields": (
                    "position",
                    "line",
                ),
            },
        ),
    )

    filter_horizontal = (
        "position",
        "line",
    )
