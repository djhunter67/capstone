# Generated by Django 4.0.1 on 2022-02-02 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hunter_diy_garage', '0006_delete_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricity_used', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('hours_used', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('auto_bay_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservations', to='hunter_diy_garage.autobay')),
                ('diy_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
