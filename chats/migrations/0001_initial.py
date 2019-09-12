# Generated by Django 2.1.7 on 2019-03-19 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.SlugField(unique=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chats')),
                ('recipient', models.ForeignKey(on_delete=None, related_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=None, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]