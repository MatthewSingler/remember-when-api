from django.db import models
class Category(models.Model):
    # Generally speaking... any type I'm working with a Type I'm using ChoiceField. 
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#choices
    # This might also be an area where you'd want to add db_index=True which will speed up search results. 
    # Starting to think about indices is more intermediate-level aspect of programming and at small-scale doesn't really matter
    # but will make/break scaling applications and having some baseline understanding will pay huge dividends. 
    # When we see engineer using indices during interview process it's a big green flag. 
    type = models.CharField(max_length=40)
