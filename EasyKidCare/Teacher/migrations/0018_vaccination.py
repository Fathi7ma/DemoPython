# Generated by Django 4.1.2 on 2023-02-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0017_rename_foodshedule_foodshedule_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='vaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=20)),
                ('VaccinationName', models.CharField(max_length=20)),
                ('Place', models.CharField(max_length=20)),
            ],
        ),
    ]