# Generated by Django 4.2.6 on 2023-11-01 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_business_teg1_business_teg2_business_teg3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='teg2',
        ),
        migrations.RemoveField(
            model_name='business',
            name='teg3',
        ),
        migrations.RemoveField(
            model_name='business',
            name='teg4',
        ),
        migrations.RemoveField(
            model_name='business',
            name='teg5',
        ),
    ]