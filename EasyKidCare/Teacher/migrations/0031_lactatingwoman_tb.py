# Generated by Django 4.1.2 on 2023-02-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0030_mother_tb_thr'),
    ]

    operations = [
        migrations.CreateModel(
            name='LactatingWoman_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Dob', models.CharField(max_length=20)),
                ('Phoneno', models.CharField(max_length=20)),
                ('Deliverydate', models.CharField(max_length=20)),
                ('Infantgender', models.CharField(max_length=20)),
            ],
        ),
    ]