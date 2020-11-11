from django.db import models


class CoreModel(models.Model):

    """ CoreModel Definition """

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
