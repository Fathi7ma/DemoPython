# Generated by Django 4.1.5 on 2023-04-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='abc', upload_to='gallery'),
            preserve_default=False,
        ),
    ]