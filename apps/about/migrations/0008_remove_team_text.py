# Generated by Django 4.2.7 on 2023-11-05 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_team_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='text',
        ),
    ]