# Generated by Django 4.1.3 on 2023-08-13 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_alter_sobre_mi_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sobre_mi",
            name="imagen",
            field=models.ImageField(upload_to="sobre", verbose_name="IMAGEN"),
        ),
    ]
