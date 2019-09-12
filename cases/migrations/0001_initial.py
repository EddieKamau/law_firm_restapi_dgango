# Generated by Django 2.1.7 on 2019-03-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('firm', '0003_auto_20190322_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=50)),
                ('case_details', models.TextField()),
                ('case_no', models.CharField(max_length=50)),
                ('case_status', models.BooleanField(default=True)),
                ('case_type', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=None, to='firm.Client')),
                ('lawyer', models.ForeignKey(on_delete=None, to='firm.Lawyer')),
            ],
        ),
    ]
