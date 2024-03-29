# Generated by Django 2.2.5 on 2019-09-08 09:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0009_auto_20190908_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
