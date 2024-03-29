# Generated by Django 2.1.7 on 2019-03-22 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firm', '0002_auto_20190321_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=10)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='activationkeys',
            name='owner',
            field=models.ForeignKey(on_delete=None, to='firm.Client'),
        ),
    ]
