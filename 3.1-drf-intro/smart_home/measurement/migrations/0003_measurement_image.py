# Generated by Django 4.1.4 on 2022-12-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_measure_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
