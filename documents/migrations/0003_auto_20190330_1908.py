# Generated by Django 2.1.7 on 2019-03-30 19:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20190325_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='target', to=settings.AUTH_USER_MODEL),
        ),
    ]
