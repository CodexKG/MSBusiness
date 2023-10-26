# Generated by Django 4.2.6 on 2023-10-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_advantage_remove_advantages_context_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advantages',
            name='more_details4',
        ),
        migrations.RemoveField(
            model_name='advantages',
            name='more_details_text4',
        ),
        migrations.AddField(
            model_name='advantage',
            name='more_details1',
            field=models.CharField(default=1, max_length=155, verbose_name='Загаловка - 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advantage',
            name='more_details_text1',
            field=models.TextField(default=1, verbose_name='Описание - 1'),
            preserve_default=False,
        ),
    ]