# Generated by Django 4.0.1 on 2022-02-09 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diy_users', '0004_alter_diyusers_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='diyusers',
            name='reservation',
            field=models.BooleanField(default=False),
        ),
    ]
