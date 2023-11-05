# Generated by Django 4.2.7 on 2023-11-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_ourprojects_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourprojects',
            name='descriptio',
        ),
        migrations.AddField(
            model_name='ourprojects',
            name='descriptio1',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер колонки - 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ourprojects',
            name='descriptio2',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер колонки - 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ourprojects',
            name='descriptio3',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер колонки - 3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ourprojects',
            name='descriptio4',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер колонки - 4'),
            preserve_default=False,
        ),
    ]