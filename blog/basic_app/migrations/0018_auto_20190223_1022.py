# Generated by Django 2.1.7 on 2019-02-23 04:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0017_auto_20190223_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 23, 4, 52, 50, 356394, tzinfo=utc)),
        ),
    ]
