from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Rewiew)
class RewiewAdmin(admin.ModelAdmin):

    """ Rewiew Admin Definition """

    pass
