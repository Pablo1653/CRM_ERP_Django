# Generated by Django 4.2 on 2023-07-18 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proveedor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proveedor",
            name="area_proveedor",
            field=models.CharField(
                choices=[
                    ("agua", "Agua"),
                    ("mineria", "Minería"),
                    ("azucar", "Azúcar"),
                    ("gas", "Gas"),
                    ("Oil & gas UP", "Oil & Gas UP"),
                    ("Oil & gas DP", "Oil & Gas DP"),
                    ("eolica", "Eólica"),
                    ("solar", "Solar"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="proveedor",
            name="pais_proveedor",
            field=models.CharField(
                choices=[
                    ("AR", "Argentina"),
                    ("BR", "Brasil"),
                    ("CL", "Chile"),
                    ("CO", "Colombia"),
                    ("MX", "México"),
                    ("PE", "Perú"),
                ],
                max_length=100,
            ),
        ),
    ]