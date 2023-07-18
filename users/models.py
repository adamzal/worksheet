from django.db import models
from django.core.exceptions import MinLengthValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class NextUser(AbstractUser):

    name = models.CharField(max_length = 20)    
    surname = models.CharField(max_length = 30)         

    payroll_number = models.PositiveIntegerField(unique = True, validators = [MinLengthValidator(limit_value = 8)])
    bonus_number = models.CharField(max_length=3, validators = [MinLengthValidator(limit_value = 3)])

