# Generated by Django 4.2.6 on 2023-10-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_remove_applications_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Заголовка'),
            preserve_default=False,
        ),
    ]