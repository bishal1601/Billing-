# Generated by Django 5.1 on 2024-10-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_alter_profile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('cashier', 'Cashier'), ('admin', 'Admin')], default='cashier', max_length=20),
        ),
    ]
