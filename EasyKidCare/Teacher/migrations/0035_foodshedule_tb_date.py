# Generated by Django 4.1.2 on 2023-03-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0034_activity_tb_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodshedule_tb',
            name='Date',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
