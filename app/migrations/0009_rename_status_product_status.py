# Generated by Django 5.1 on 2024-08-20 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Status',
            new_name='status',
        ),
    ]
