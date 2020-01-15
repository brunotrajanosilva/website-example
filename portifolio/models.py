from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Bedroom(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(max_length=2000)
    image = models.FileField(upload_to="bedroom_images")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.FileField(upload_to="team")

    def __str__(self):
        return self.name