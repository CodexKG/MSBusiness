# Generated by Django 4.2.7 on 2023-11-05 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_details_team_kolonki_details_team_kolonki2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='context',
            new_name='context_text',
        ),
    ]
