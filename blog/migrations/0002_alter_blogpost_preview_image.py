# Generated by Django 5.1.4 on 2025-02-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='preview_image',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]
