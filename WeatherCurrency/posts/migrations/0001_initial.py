# Generated by Django 4.2.7 on 2023-11-30 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=300)),
                ('date', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]
