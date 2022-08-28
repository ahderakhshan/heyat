from django.db import models

# Create your models here.


class Ceremony(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField()
    title_img = models.ImageField(null=True, upload_to='media/title_images')
    date = models.DateField(auto_now=True)


class Picture(models.Model):
    img = models.ImageField(upload_to='media/ceremony_images')
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE)


class Audio(models.Model):
    audio = models.FileField(upload_to='audios')
    ceremony = models.ForeignKey(Ceremony, on_delete=models.CASCADE)


class Namahang(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='video')
