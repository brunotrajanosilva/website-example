from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100, null=True)
    alt = models.CharField(max_length=200)
    src = models.ImageField(upload_to="images/")

    def __str__(self):
        # return mark_safe(f'<img height="100" src="{self.src.url}" />')
        return self.name


class Bedroom(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(max_length=2000)
    bedroom_image = models.OneToOneField(Image, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.FileField(upload_to="team/")

    def __str__(self):
        return self.name