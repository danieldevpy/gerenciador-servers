# Generated by Django 5.0.3 on 2024-04-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0016_remove_program_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='password',
            field=models.BooleanField(default=False, null=True),
        ),
    ]