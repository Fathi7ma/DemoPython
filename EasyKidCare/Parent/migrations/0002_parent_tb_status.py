# Generated by Django 4.1.2 on 2022-12-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent_tb',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]