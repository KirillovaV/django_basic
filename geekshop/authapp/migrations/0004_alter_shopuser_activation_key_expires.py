# Generated by Django 3.2.6 on 2021-10-08 05:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20211006_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 5, 4, 29, 504870, tzinfo=utc), verbose_name='актуальность'),
        ),
    ]