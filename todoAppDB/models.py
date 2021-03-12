from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    state = models.BooleanField()
    priority = models.IntegerField()

