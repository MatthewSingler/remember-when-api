from django.db import models
from django.contrib.auth.models import User
class Fact(models.Model):
    year = models.ForeignKey("Year", on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    is_approved = models.BooleanField()
    category = models.ManyToManyField("Category", through="FactCategory", related_name="Type")
    user = models.ForeignKey(User, on_delete=models.CASCADE)