# Generated by Django 2.0b1 on 2017-11-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20171108_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagethree',
            name='name_kino',
            field=models.CharField(max_length=60, verbose_name='Название фильма'),
        ),
    ]
