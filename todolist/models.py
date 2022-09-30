from django.db import models

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField()
    date = models.DateField()
    title = models.CharField(max_length=256)