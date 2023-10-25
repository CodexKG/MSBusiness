# Generated by Django 4.2.6 on 2023-10-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0034_foote_context2_foote_context3_footer_title2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foote',
            name='context3',
        ),
        migrations.AddField(
            model_name='foote',
            name='image',
            field=models.ImageField(default=11, max_length='Фото футера', upload_to='services/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foote',
            name='context',
            field=models.CharField(max_length=255, verbose_name='Подзаголовок 1 Услуги'),
        ),
        migrations.AlterField(
            model_name='foote',
            name='context2',
            field=models.CharField(max_length=255, verbose_name='Подзаголовок 2 Услуги'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовка - 1'),
        ),
    ]
