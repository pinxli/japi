# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_remove_paymenttype_request_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
