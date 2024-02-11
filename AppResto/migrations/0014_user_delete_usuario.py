# Generated by Django 5.0.1 on 2024-01-18 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppResto', '0013_alter_reseña_fecha_de_reseña_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]