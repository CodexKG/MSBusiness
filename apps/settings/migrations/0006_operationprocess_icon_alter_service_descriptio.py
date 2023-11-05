# Generated by Django 4.2.7 on 2023-11-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_service_descriptio'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationprocess',
            name='icon',
            field=models.CharField(choices=[('ИЗУЧЕНИЕ', 'ИЗУЧЕНИЕ'), ('РАЗРАБОТКА', 'РАЗРАБОТКА'), ('ЗАПУСК', 'ЗАПУСК')], default=1, max_length=50, verbose_name='Выберите Иконку'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='descriptio',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
