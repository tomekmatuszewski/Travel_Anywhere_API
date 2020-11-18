# Generated by Django 3.1.3 on 2020-11-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel_anywhere", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="continent",
            name="name",
            field=models.CharField(
                choices=[
                    ("Europe", "Europe"),
                    ("North America", "North Am"),
                    ("South America", "South Am"),
                    ("Asia", "Asia"),
                    ("Australia & Oceania", "Aus Oceania"),
                    ("Africa", "Africa"),
                ],
                max_length=32,
                unique=True,
            ),
        ),
    ]
