from django.db import models
from core import models as core_model


class Tip(core_model.CoreModel):

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tips", null=True
    )
    champion = models.ForeignKey(
        "champions.Champion", on_delete=models.CASCADE, related_name="tips", null=True
    )
    recommand = models.IntegerField(null=True, default=0)
    description = models.TextField()

    def __str__(self):
        return f"{self.champion} Tip"
