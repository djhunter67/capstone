# Generated by Django 4.0.1 on 2022-01-27 02:22

import diy_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diy_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diyusers',
            name='avatar',
            field=models.ImageField(default='../static/img/default_avt.png', upload_to=diy_users.models.upload_path),
        ),
    ]
