from django.db import models
from django.contrib.auth.models import User
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Should this just be a TextField with no length limitation within DB? If you want a length limitation I'd recommend 
    # enforcing at the Django form / React widget level to future-proof this. 
    contents = models.CharField(max_length=500)
    fact = models.ForeignKey("Fact", on_delete=models.CASCADE)
