# Generated by Django 4.0.1 on 2022-02-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter_diy_garage', '0004_alter_reservation_electricity_used_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
