# Generated by Django 5.0.3 on 2024-04-12 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_config_ip_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='NginxBackup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 12, 14, 13, 31, 524398), null=True)),
                ('content', models.TextField()),
            ],
        ),
    ]