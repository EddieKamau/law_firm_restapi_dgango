# Generated by Django 2.1.7 on 2019-03-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20190320_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
