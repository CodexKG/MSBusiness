# Generated by Django 4.2.7 on 2023-11-04 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=155, null=True, verbose_name='Номер Телефона')),
                ('email', models.CharField(blank=True, max_length=155, null=True, verbose_name='Адресс почты')),
                ('limit', models.CharField(max_length=155, verbose_name='Лимит')),
                ('message', models.CharField(max_length=155, verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Контакты и заявка',
            },
        ),
        migrations.CreateModel(
            name='Gellary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Галлерея',
            },
        ),
        migrations.CreateModel(
            name='OperationProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='process', verbose_name='фото')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('descriptions', models.CharField(max_length=300, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Процесс работы',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('description', models.CharField(max_length=255, verbose_name='описание')),
                ('image', models.ImageField(upload_to='partner', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Наши проекты',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('descriptio', models.CharField(max_length=155, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='service', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовка')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Фото')),
                ('email', models.CharField(blank=True, max_length=155, null=True, verbose_name='Адрес почты')),
                ('phone', models.CharField(blank=True, max_length=155, null=True, verbose_name='Номер Телефона')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('schedule', models.CharField(blank=True, max_length=155, null=True, verbose_name='Расписание')),
                ('facebook', models.CharField(blank=True, max_length=155, null=True, verbose_name='Файсбук')),
                ('skype', models.CharField(blank=True, max_length=155, null=True, verbose_name='Скайп')),
                ('instagram', models.CharField(blank=True, max_length=155, null=True, verbose_name='Инстаграмм')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настройки Всего',
            },
        ),
        migrations.CreateModel(
            name='ProjectoFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_us_images', to='settings.project')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Особенности проекта',
            },
        ),
    ]