# Generated by Django 4.1.3 on 2023-08-13 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web_2", "0008_modelos_url_git_alter_modelos_imagen"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="modelos",
            options={
                "ordering": ["-created"],
                "verbose_name": "Modelo",
                "verbose_name_plural": "Modelos",
            },
        ),
    ]