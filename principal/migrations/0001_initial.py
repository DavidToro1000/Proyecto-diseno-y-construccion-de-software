# Generated by Django 4.2.7 on 2023-11-09 20:29

from django.db import migrations, models

def anadirDatosIniciales(apps, schema_editor):
    Sector = apps.get_model('principal', 'Sector')
    sectores_iniciales = ['Sector1', 'Sector2', 'Sector3', 'Sector4', 'Sector5']

    for nombre_sector in sectores_iniciales:
        Sector.objects.create(nombre=nombre_sector)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            
        ),
        migrations.RunPython(anadirDatosIniciales)
    ]
