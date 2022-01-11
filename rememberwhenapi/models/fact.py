from django.db import models
from django.contrib.auth.models import User
class Fact(models.Model):
    # Probably a great place for db_index as you'll presumably be filtering/searching on year/date. 
    year = models.ForeignKey("Year", on_delete=models.CASCADE, related_name='facts')
    # See Comment comment, probably want this to be TextField unless really good reason to limit it in the DB.
    contents = models.CharField(max_length=500)
    is_approved = models.BooleanField()
    # I don't think you want related_name to be capitalized, goes against Django/Python standard if memory serves. 
    category = models.ManyToManyField("Category", through="FactCategory", related_name="Type")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
