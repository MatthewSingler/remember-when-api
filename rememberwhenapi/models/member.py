from django.db import models
from django.contrib.auth.models import User
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.BooleanField()
