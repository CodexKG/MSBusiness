# Generated by Django 4.2.6 on 2023-10-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_remove_status_context2_remove_status_context3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='status_icon',
            field=models.CharField(choices=[('Довольных Клиенты', 'Довольных Клиенты'), ('Опытных сотрудников', 'Опытных сотрудников'), ('Удовлетворенности', 'Удовлетворенности'), ('Наград', 'Наград')], default=1, max_length=50, verbose_name='Выберите иконку'),
            preserve_default=False,
        ),
    ]