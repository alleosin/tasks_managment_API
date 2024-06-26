from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=150)
    phone = models.CharField(max_length=16, unique=True)

