# Generated by Django 4.1.3 on 2022-11-16 19:04

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TOA',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('toa_name', models.CharField(max_length=200)),
                ('toa_summary', models.CharField(max_length=1000)),
                ('toa_contact', models.CharField(max_length=200)),
                ('toa_latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90.0), django.core.validators.MaxValueValidator(90.0)])),
                ('toa_longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180.0), django.core.validators.MaxValueValidator(180.0)])),
                ('image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]