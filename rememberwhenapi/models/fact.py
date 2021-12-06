from django.db import models
class Fact(models.Model):
    year_Id = models.ForeignKey("Year", on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    is_Approved = models.BooleanField(default=true)