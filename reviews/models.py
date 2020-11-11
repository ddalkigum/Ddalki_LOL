from django.db import models
from core import models as core_model


class Review(core_model.CoreModel):

    name = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="reviews", null=True
    )
    photo = models.ImageField(upload_to="review_image", blank=True)
    rating = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.product} Review"
