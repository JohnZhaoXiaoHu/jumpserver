# Generated by Django 3.2.17 on 2023-06-30 09:04

import common.db.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0063_auto_20230621_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='rdp7_port',
            field=common.db.fields.PortField(default=3390, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)], verbose_name='RDP7 port'),
        ),
    ]