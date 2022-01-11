# Need two lines between imports and your class, otherwise would fail Flake8 (look it up) style guide. 
from django.db import models
class FactCategory(models.Model):
    # I can't figure out why this model exists... seems redundant. Why not just have Facts and Categories and let people filter accordingly?
    fact = models.ForeignKey("Fact", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
