# Generated by Django 2.1.7 on 2019-02-21 15:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_auto_20190221_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='created_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 34, 47, 583862, tzinfo=utc)),
        ),
    ]
