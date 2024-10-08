# Generated by Django 5.1 on 2024-09-27 16:35

import app.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_stockmovement_sdate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Holdsale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(choices=app.models.Product.get_product_choices, max_length=255)),
                ('opid', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(choices=app.models.Unit.get_unit_choices, max_length=255)),
                ('channel', models.CharField(max_length=20)),
                ('invoice', models.IntegerField(blank=True, null=True)),
                ('vendor', models.CharField(blank=True, choices=app.models.Vendor.get_vendor_choices, max_length=255, null=True)),
                ('pdate', models.DateField(blank=True, null=True)),
                ('sdate', models.DateField(auto_now_add=True, null=True)),
                ('User', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
