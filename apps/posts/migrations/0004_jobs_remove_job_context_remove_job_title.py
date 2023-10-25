# Generated by Django 4.2.6 on 2023-10-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=355, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Заголовка Работы ',
            },
        ),
        migrations.RemoveField(
            model_name='job',
            name='context',
        ),
        migrations.RemoveField(
            model_name='job',
            name='title',
        ),
    ]
