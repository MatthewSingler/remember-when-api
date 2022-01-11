from django.db import models
class Category(models.Model):
    # Generally speaking... any type I'm working with a Type I'm using ChoiceField. 
    # https://docs.djangoproject.com/en/4.0/ref/models/fields/#choices
    type = models.CharField(max_length=40)
