# Generated by Django 4.1.2 on 2023-02-04 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0018_vaccination'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vaccination',
            new_name='vaccination_tb',
        ),
    ]