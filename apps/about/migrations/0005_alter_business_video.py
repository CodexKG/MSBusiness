# Generated by Django 4.2.7 on 2023-11-05 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='video',
            field=models.URLField(verbose_name='Видео'),
        ),
    ]