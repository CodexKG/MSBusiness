# Generated by Django 4.2.6 on 2023-10-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='main',
            options={'verbose_name': '', 'verbose_name_plural': 'Заголовка Услуги'},
        ),
        migrations.AddField(
            model_name='main',
            name='title1',
            field=models.CharField(default=1, max_length=155, verbose_name='Главная'),
            preserve_default=False,
        ),
    ]