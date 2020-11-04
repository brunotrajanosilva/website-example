from django.contrib import admin
from .models import Bedroom, Team, Image
from django.utils.html import mark_safe

# Register your models here.

admin.site.register(Team)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'alt', 'img')

    def img(self, obj):
        return mark_safe(f'<img height="100" src="{obj.src.url}" />')



@admin.register(Bedroom)
class BedroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description_', 'img')

    def img(self, obj):
        return mark_safe(f'<img height="100" src="{obj.bedroom_image.src.url}" />')

    def description_(self, obj):
        return mark_safe(f'<article>{obj.description}</article>')