from django.db import models
from django.contrib.auth.models import User
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # For booleans it's our Ambition best-practice to always prepend with "is_" to make it very clear it's a toggle. 
    # Otherwise could this be a FK to another User Model and this is a relationship between an actual Admin and User? Kinda like their manager?
    admin = models.BooleanField()
