# Generated by Django 5.1 on 2024-08-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_full_name_unit_fullname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='Status',
            field=models.BooleanField(default=True),
        ),
    ]
