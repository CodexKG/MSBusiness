# Generated by Django 4.2.7 on 2023-11-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка')),
                ('context', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='details', verbose_name='Фото')),
                ('kolonki', models.CharField(blank=True, max_length=155, null=True, verbose_name='Колонки Блога')),
                ('review_blog', models.CharField(blank=True, max_length=155, null=True, verbose_name='Блог Услуги')),
                ('business_blog', models.CharField(blank=True, max_length=155, null=True, verbose_name='Заголовка')),
                ('business_context', models.CharField(blank=True, max_length=300, null=True, verbose_name='Описание Бизнеса')),
                ('business_image', models.ImageField(blank=True, null=True, upload_to='business', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настрокий детального Услуги',
            },
        ),
    ]
