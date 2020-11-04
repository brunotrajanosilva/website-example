# Generated by Django 3.1.1 on 2020-10-07 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0004_auto_20200113_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('alt', models.CharField(max_length=200)),
                ('src', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='bedroom',
            name='image',
        ),
        migrations.AddField(
            model_name='bedroom',
            name='bedroom_image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portifolio.image'),
        ),
    ]
