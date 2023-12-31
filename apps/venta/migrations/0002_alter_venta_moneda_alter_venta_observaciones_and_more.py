# Generated by Django 4.2 on 2023-07-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("venta", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venta",
            name="moneda",
            field=models.CharField(
                choices=[
                    ("EURO", "EURO"),
                    ("DOLAR", "DOLAR"),
                    ("PESO ARGENTINO", "PESO ARGENTINO"),
                    ("PESO COLOMBIANO", "PESO COLOMBIANO"),
                    ("PESO CHILENO", "PESO CHILENO"),
                    ("SOL PERUANO", "SOL PERUANO"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="venta",
            name="observaciones",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="venta", name="tipo_cambio", field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="venta", name="utilidad_esperada", field=models.FloatField(),
        ),
    ]
