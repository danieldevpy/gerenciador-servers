# Generated by Django 5.0.3 on 2024-04-09 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nginx', '0002_config_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.RemoveField(
            model_name='config',
            name='user',
        ),
    ]
