# Generated by Django 4.2.6 on 2023-10-24 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_min_about_remove_main_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='min_about',
            name='title',
            field=models.CharField(default=1, max_length=1, verbose_name='QWERTYU'),
            preserve_default=False,
        ),
    ]