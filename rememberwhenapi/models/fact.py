from django.db import models
class Fact(models.Model):
    year = models.ForeignKey("Year", on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    is_approved = models.BooleanField()