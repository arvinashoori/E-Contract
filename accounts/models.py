from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, verbose_name="Email Address")
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username