# Generated by Django 4.1.5 on 2023-04-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0036_teacher_tb_confirmpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_tb',
            name='confirmpassword',
            field=models.CharField(max_length=20),
        ),
    ]
