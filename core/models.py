from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ TIME ATAMPED MODEL """

    created_at = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
