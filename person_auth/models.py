from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class Number(models.Model):
    user = models.ForeignKey(User)
    phone_regex = RegexValidator(regex=r'\+?\d{11}$',
                                 message="Номеру повинен бути виду +380000000000.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=13, verbose_name="Номер телефону")

    def __str__(self):
        return self.phone_number
