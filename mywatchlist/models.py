from django.db import models

class Movie(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=256)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.CharField(max_length=8192)