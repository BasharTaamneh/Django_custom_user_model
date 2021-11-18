from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15,  unique=False,  blank=True)
    age = models.CharField(max_length=2,  unique=False, blank=True)

    def __str__(self):
        return self.username