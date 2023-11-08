# Generated by Django 4.2.7 on 2023-11-08 15:59

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Имя пользователя')),
                ('phone', models.CharField(max_length=155, verbose_name='Номер телефона')),
                ('message', models.TextField(verbose_name='Введите ваше сообщение')),
            ],
            options={
                'verbose_name': 'Оставленный отзыв доктору',
                'verbose_name_plural': 'Оставленный отзыв доктору',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_team', models.CharField(max_length=100, verbose_name='ID пользователя telegram')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('job', models.CharField(max_length=255, verbose_name='Должность')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='teacher_img/', verbose_name='Фотография')),
                ('descriptions', models.TextField(max_length=255, verbose_name='Описание человека')),
                ('phone_doctor', models.CharField(blank=True, max_length=255, null=True, verbose_name='номер')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
            ],
            options={
                'verbose_name': 'Наша команда',
                'verbose_name_plural': 'Наша команда',
            },
        ),
    ]
