# Generated by Django 4.1.2 on 2023-02-11 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Parent', '0011_student_tb_parentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccination_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=20)),
                ('VaccinationName', models.CharField(max_length=20)),
                ('Place', models.CharField(max_length=20)),
                ('studentid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Parent.student_tb')),
            ],
        ),
    ]
