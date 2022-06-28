from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """TIME STAMPED MODEL"""

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
