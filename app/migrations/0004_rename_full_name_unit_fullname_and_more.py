# Generated by Django 5.1 on 2024-08-17 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_unit_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='Full_Name',
            new_name='FullName',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='Short_Name',
            new_name='ShortName',
        ),
    ]
