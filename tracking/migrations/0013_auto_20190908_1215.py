# Generated by Django 2.2.5 on 2019-09-08 09:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0012_auto_20190908_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator('^\\d{11}$')], verbose_name='Telefon Numarası'),
        ),
        migrations.AlterField(
            model_name='tracking',
            name='tracking_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')], verbose_name='Takip Kodu'),
        ),
    ]
