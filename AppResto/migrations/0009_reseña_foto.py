# Generated by Django 5.0.1 on 2024-01-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResto', '0008_alter_restaurante_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseña',
            name='foto',
            field=models.ImageField(default='1', upload_to='AppResto/img/'),
            preserve_default=False,
        ),
    ]
