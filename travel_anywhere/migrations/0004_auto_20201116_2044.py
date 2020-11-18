# Generated by Django 3.1.3 on 2020-11-16 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel_anywhere", "0003_auto_20201116_2036"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trip",
            name="destination_airport",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="trips_destination",
                to="travel_anywhere.airport",
            ),
        ),
    ]
