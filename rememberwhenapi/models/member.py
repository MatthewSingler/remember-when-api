from django.db import models
from django.contrib.auth.models import User
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # For booleans it's our Ambition best-practice to always prepend with "is_" to make it very clear it's a toggle. 
    admin = models.BooleanField()
