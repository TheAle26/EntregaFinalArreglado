# Generated by Django 5.0.1 on 2024-01-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResto', '0007_restaurante_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='foto',
            field=models.ImageField(upload_to='AppResto/img/'),
        ),
    ]