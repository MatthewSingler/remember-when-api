from django.db import models
class Year(models.Model):
    # I don't know what but there's got to be a more robust way to do this than just manually storing year as integer like this. 
    # First glance I would _probably_ still use Django DateField but just store as 1986-1-1 and then filter on just year__equals=<search_string>. 
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#datefield
    # This will greatly future-proof for if/when you want to intoduce more granularity and you won't have to worry about a non-trivial data migration. 
    year_number = models.IntegerField()
    
