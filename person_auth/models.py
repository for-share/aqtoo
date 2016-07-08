from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Number(models.Model):
    user = models.ForeignKey(User)
    phone_number = PhoneNumberField(max_length=20)
    date_create = models.DateTimeField(auto_now_add=True)
    date_of_processing = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return str(self.phone_number)
