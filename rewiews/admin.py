from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Rewiew)
class RewiewAdmin(admin.ModelAdmin):

    """ Rewiew Admin Definition """

    list_display = ("__str__", "rating_average")
