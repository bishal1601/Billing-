# Generated by Django 5.1 on 2024-08-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_stock_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('channel', models.CharField(max_length=20)),
            ],
        ),
    ]
