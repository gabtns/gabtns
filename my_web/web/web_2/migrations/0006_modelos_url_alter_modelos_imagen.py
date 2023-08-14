# Generated by Django 4.1.3 on 2023-08-07 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_2", "0005_remove_modelos_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelos",
            name="url",
            field=models.URLField(default=1, verbose_name="url"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="modelos",
            name="imagen",
            field=models.ImageField(upload_to="web2", verbose_name="IMAGEN"),
        ),
    ]