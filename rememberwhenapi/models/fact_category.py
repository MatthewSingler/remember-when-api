from django.db import models
class FactCategory(models.Model):
    fact_id = models.ForeignKey("Fact", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
