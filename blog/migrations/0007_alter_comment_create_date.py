# Generated by Django 3.2.5 on 2022-04-21 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220421_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 14, 35, 0, 820296, tzinfo=utc)),
        ),
    ]
