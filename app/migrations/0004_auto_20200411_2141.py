# Generated by Django 3.0.4 on 2020-04-12 01:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200409_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='ends_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 21, 41, 16, 160393)),
        ),
    ]
