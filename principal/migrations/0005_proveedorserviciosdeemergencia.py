# Generated by Django 4.2.7 on 2023-11-14 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_sistematrafico'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProveedorServiciosDeEmergencia',
            fields=[
                ('contacto', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]