# Generated by Django 2.1.7 on 2019-02-21 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20190221_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='created_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 20, 52, 397636, tzinfo=utc)),
        ),
    ]
