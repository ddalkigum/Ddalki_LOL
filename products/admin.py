from django.contrib import admin
from . import models


@admin.register(models.Meterial)
class MeterialAdmin(admin.ModelAdmin):

    list_display = ("__str__",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("__str__",)


@admin.register(models.Origin)
class OriginAdmin(admin.ModelAdmin):

    list_display = ("__str__",)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    """ Product Admin Definition """

    list_display = (
        "name",
        "price",
        "category",
        "origin",
        "soldout",
    )

    fieldsets = (
        (
            "Product Basic",
            {
                "fields": (
                    "name",
                    "price",
                    "description",
                    "soldout",
                    "image",
                ),
            },
        ),
        (
            "Configuration",
            {
                "fields": (
                    "material",
                    "category",
                    "origin",
                ),
            },
        ),
    )

    filter_horizontal = ("material",)
