# Generated by Django 4.0.4 on 2022-04-24 01:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_fill_amount_alter_fuelpump_priceperliter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='currentFuel',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(models.FloatField())]),
        ),
        migrations.AlterField(
            model_name='tank',
            name='maxCapacity',
            field=models.FloatField(),
        ),
    ]
