# Generated by Django 4.1.2 on 2023-02-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0027_mother_tb_nutritions'),
    ]

    operations = [
        migrations.AddField(
            model_name='mother_tb',
            name='Dob',
            field=models.CharField(default='abc', max_length=20),
        ),
    ]
