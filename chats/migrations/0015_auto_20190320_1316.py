# Generated by Django 2.1.7 on 2019-03-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0014_auto_20190320_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
