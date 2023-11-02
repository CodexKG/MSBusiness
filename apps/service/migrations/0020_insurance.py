# Generated by Django 4.2.6 on 2023-11-02 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_style6'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=255, verbose_name='Описание')),
                ('text', models.TextField(verbose_name='Текст')),
                ('blog_title', models.CharField(max_length=255, verbose_name='Заголовка Блога')),
                ('blog_context', models.CharField(max_length=300, verbose_name='Описание Блога')),
                ('image', models.ImageField(upload_to='insurance/', verbose_name='Фото')),
                ('icon', models.CharField(choices=[('Страхование путешествий', 'Страхование путешествий'), ('Медицинский Страхование', 'Медицинский Страхование'), ('Страхование брака', 'Страхование брака'), ('Страхование жизни', 'Страхование жизни'), ('Страхование дома', 'Страхование дома'), ('Страховка от пожара', 'Страховка от пожара')], max_length=100, verbose_name='Выберите иконку')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Страхование',
            },
        ),
    ]
