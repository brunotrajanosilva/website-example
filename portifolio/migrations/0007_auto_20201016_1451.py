# Generated by Django 3.1.1 on 2020-10-16 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0006_auto_20201009_2259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='name',
        ),
    ]
