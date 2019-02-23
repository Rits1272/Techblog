# Generated by Django 2.1.7 on 2019-02-21 14:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20190221_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='text',
            field=models.TextField(default=datetime.datetime(2019, 2, 21, 14, 18, 19, 26798, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ask',
            name='created_data',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 14, 18, 0, 866364, tzinfo=utc)),
        ),
    ]
