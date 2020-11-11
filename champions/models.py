from django.db import models
from core import models as core_model


class AbsractModel(core_model.CoreModel):

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Position(AbsractModel):
    def __str__(self):
        return self.name


class Line(AbsractModel):
    def __str__(self):
        return self.name


class Champion(core_model.CoreModel):

    """ Champion Model Definition """

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    square_image = models.ImageField(upload_to="champion_image", blank=True)
    loading_image = models.ImageField(upload_to="champion_image", blank=True)
    bio = models.TextField()
    position = models.ManyToManyField("Position", blank=True, related_name="champions")
    line = models.ManyToManyField("Line", blank=True, related_name="champions")

    def __str__(self):
        return self.name
