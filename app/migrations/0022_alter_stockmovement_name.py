# Generated by Django 5.1 on 2024-08-23 05:01

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_stockmovement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmovement',
            name='name',
            field=models.CharField(choices=app.models.Product.get_product_choices, max_length=255),
        ),
    ]
