# Generated by Django 4.1.7 on 2023-02-17 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_alter_photographies_photo_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographies',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]