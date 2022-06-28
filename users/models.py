from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    """ CUTOM USER MODEL """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other")
    )

    LANGUADGE_ENGLISH = 'en'
    LANGUADGE_KOREAN = 'kr'

    LANGUADGE_CHOICES = (
        (LANGUADGE_ENGLISH, "English"),
        (LANGUADGE_KOREAN, "Korean")
    )

    CURRENCY_USD = 'usd'
    CURRENCY_KRW = 'krw'

    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_KRW, 'KRW')
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    languadge = models.CharField(
        choices=LANGUADGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
    
