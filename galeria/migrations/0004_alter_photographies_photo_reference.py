# Generated by Django 4.1.7 on 2023-02-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_rename_photography_photographies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographies',
            name='photo_reference',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
