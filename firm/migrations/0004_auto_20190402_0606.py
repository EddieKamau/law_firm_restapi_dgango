# Generated by Django 2.1.7 on 2019-04-02 06:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firm', '0003_auto_20190322_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationkeys',
            name='owner',
            field=models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
