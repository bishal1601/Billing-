# Generated by Django 5.1 on 2024-08-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_stockmovement_sdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmovement',
            name='sdate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
