# Generated by Django 5.1 on 2024-08-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_units_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='Full_Name',
            field=models.CharField(max_length=100),
        ),
    ]
