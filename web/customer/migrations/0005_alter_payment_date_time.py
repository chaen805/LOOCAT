# Generated by Django 4.0.4 on 2022-06-08 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_payment_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 11, 7, 19, 843492)),
        ),
    ]