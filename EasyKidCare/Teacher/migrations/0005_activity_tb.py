# Generated by Django 4.1.2 on 2022-12-24 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0004_teacher_tb_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActionSong', models.CharField(max_length=20)),
                ('Drawing', models.CharField(max_length=20)),
                ('Studying', models.CharField(max_length=20)),
                ('SleepingTime', models.CharField(max_length=20)),
            ],
        ),
    ]