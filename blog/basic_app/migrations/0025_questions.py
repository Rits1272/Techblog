# Generated by Django 2.1.7 on 2019-03-01 03:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0024_auto_20190228_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=15)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.TextField()),
            ],
        ),
    ]
