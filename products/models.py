from django.db import models
from core import models as core_model


class AbstractModel(core_model.CoreModel):

    name = name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Meterial(AbstractModel):

    pass


class Category(AbstractModel):

    name = models.CharField(max_length=50, default="의류")

    class Meta:
        verbose_name_plural = "Categories"


class Origin(AbstractModel):

    name = models.CharField(max_length=50, default="Korea")


class Product(core_model.CoreModel):

    """ Product Model Definition """

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="product_image", null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    material = models.ManyToManyField("Meterial", related_name="products", blank=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    origin = models.ForeignKey(
        "Origin",
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    soldout = models.BooleanField(default=False)

    def __str__(self):
        return self.name
