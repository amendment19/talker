from django.db import models

# Create your models here.
class Audio(models.Model):
    audio_file = models.CharField(max_length=30)

class Images(models.Model):
    image_file = models.CharField(max_length=30)
