from django.db import models

# Create your models here.

class Movie(models.Model):
    mid = models.IntegerField()
    title = models.CharField(max_length=20)
    mainPicSrc = models.CharField(max_length=256)
    star = models.CharField(max_length=10)
    summary=models.TextField()
    comments=models.TextField()

    def __str__(self):
        return self.title

class Character(models.Model):
    cid=models.IntegerField()
    name=models.CharField(max_length=100)
    movies=models.ManyToManyField(Movie)

    def __str__(self):
        return self.name