# Generated by Django 4.1.5 on 2023-02-02 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0013_student_tb_alter_mother_tb_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absent_tb',
            name='Studentid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher.student_tb'),
        ),
        migrations.AlterField(
            model_name='present_tb',
            name='Studentid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher.student_tb'),
        ),
    ]
