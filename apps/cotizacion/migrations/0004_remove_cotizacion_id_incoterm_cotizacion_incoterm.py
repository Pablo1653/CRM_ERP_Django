# Generated by Django 4.2 on 2023-07-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cotizacion", "0003_remove_cotizacion_incoterm_cotizacion_id_incoterm"),
    ]

    operations = [
        migrations.RemoveField(model_name="cotizacion", name="id_incoterm",),
        migrations.AddField(
            model_name="cotizacion",
            name="incoterm",
            field=models.CharField(default="", max_length=200),
        ),
    ]
