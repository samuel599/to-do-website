from django.db import models
from django.contrib.auth.models import User
from datetimepicker.widgets import DateTimePicker
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    description = models.TextField(max_length=500)
    datetime = models.DateTimeField()
    widget = DateTimePicker()
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
