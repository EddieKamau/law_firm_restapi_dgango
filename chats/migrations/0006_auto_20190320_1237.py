# Generated by Django 2.1.7 on 2019-03-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_auto_20190320_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]