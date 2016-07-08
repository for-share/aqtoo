from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Number(models.Model):
    user = models.ForeignKey(User)
    phone_number = PhoneNumberField(max_length=20)
    date_create = models.DateTimeField(auto_now_add=True)
    date_of_processing = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.phone_number
