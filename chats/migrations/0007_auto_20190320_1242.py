# Generated by Django 2.1.7 on 2019-03-20 12:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_auto_20190320_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 20, 12, 42, 18, 770029, tzinfo=utc)),
        ),
    ]
