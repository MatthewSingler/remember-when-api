from django.db import models
class Comment(models.Model):
    user_Id = models.ForeignKey("User", on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    fact_Id = models.ForeignKey("Facts", on_delete=models.CASCADE)
    