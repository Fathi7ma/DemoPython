# Generated by Django 4.1.5 on 2023-02-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Parent', '0008_parent_tb_address_delete_student_tb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent_tb',
            name='Address',
            field=models.CharField(max_length=20),
        ),
    ]
