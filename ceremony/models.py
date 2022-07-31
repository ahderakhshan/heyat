from django.db import models

# Create your models here.


class Ceremony(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField()
    date = models.DateField(auto_now=True)


class Picture(models.Model):
    img = models.ImageField()
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE)


class Audio(models.Model):
    audio = models.FileField()
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE)