# Generated by Django 3.0.1 on 2020-01-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0002_auto_20200110_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bedroom',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]