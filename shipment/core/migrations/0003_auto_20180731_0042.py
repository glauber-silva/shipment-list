# Generated by Django 2.0.7 on 2018-07-31 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180731_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='sender',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='expected_ship_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 3, 0, 42, 50, 462365)),
        ),
    ]