# Generated by Django 4.2.6 on 2023-10-25 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='image2',
        ),
    ]
