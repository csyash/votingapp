from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

from accounts.managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField("Email address", unique=True)
    aadhar = models.IntegerField('Aadhar', unique=True, null=True)
    kalinga_id = models.CharField("Kalinga ID",max_length=40, null=True )
    dob = models.DateField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "aadhar", "dob", "kalinga_id"]
    objects = CustomUserManager()

    def __str__(self):
        return self.username
