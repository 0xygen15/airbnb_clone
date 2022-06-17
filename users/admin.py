from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ CUSTOM USER ADMIN """

    list_display = ("username", "gender", "languadge", "currency", "superhost")
    list_filter = ("languadge", "superhost", "currency")
    