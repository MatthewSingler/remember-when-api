from django.db import models
class FactCategory(models.Model):
    fact = models.ForeignKey("Fact", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
