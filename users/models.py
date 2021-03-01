from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostActivity(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title
