# Generated by Django 4.2.6 on 2023-11-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricind', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('title_blog', models.CharField(max_length=155, verbose_name='Заголовка Блога')),
                ('context_blog', models.CharField(max_length=155, verbose_name='Описание Блога')),
                ('end_blog', models.CharField(max_length=100, verbose_name=' Конец Блога')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Сопровождение Бизнеса',
            },
        ),
    ]