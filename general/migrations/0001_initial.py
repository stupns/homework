# Generated by Django 2.0b1 on 2017-11-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=16, verbose_name='Имя преподователя')),
                ('user', models.CharField(max_length=16, verbose_name='Имя учасника')),
                ('data', models.DateTimeField(verbose_name='Время')),
            ],
        ),
        migrations.CreateModel(
            name='PageThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Время')),
                ('name_kino', models.DateField(verbose_name='Название фильма')),
            ],
        ),
        migrations.CreateModel(
            name='PageTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poet', models.CharField(max_length=16, verbose_name='Имя поета')),
                ('text', models.TextField(max_length=320, verbose_name='cтихотворение')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=16, verbose_name='Фамилия')),
                ('age', models.IntegerField(blank=None, verbose_name='Bозраст')),
            ],
        ),
    ]
