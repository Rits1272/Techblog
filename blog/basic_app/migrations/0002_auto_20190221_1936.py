# Generated by Django 2.1.7 on 2019-02-21 14:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='created_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 14, 6, 30, 379720, tzinfo=utc)),
        ),
    ]
