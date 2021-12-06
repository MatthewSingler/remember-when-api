from django.db import models
from django.contrib.auth.models import User
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    fact = models.ForeignKey("Fact", on_delete=models.CASCADE)
    