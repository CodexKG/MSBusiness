# Generated by Django 4.2.7 on 2023-11-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_ourprojects_descriptio1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='blog_details', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настройки Детального Блога',
            },
        ),
    ]
