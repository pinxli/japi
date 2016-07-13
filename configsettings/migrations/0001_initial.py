# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('level', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommissionSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[('0', 'Inactive'), ('1', 'Active')], default=0)),
                ('invest_least', models.IntegerField()),
                ('deposit_fee', models.IntegerField()),
                ('deposit_fee_max', models.IntegerField()),
                ('withdraw_fee', models.IntegerField()),
                ('withdraw_fee_max', models.IntegerField()),
            ],
            options={
                'db_table': 'configsettings_commissionsettings',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('threshold', models.CommaSeparatedIntegerField(max_length=10)),
                ('rate', models.IntegerField()),
                ('check_rate', models.IntegerField()),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('online_discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_online_discount', to='level.Level')),
                ('remit_discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_remit_discount', to='level.Level')),
            ],
            options={
                'db_table': 'configsettings_discount',
            },
        ),
        migrations.CreateModel(
            name='ReturnSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[('0', 'Inactive'), ('1', 'Active')], default=0)),
            ],
            options={
                'db_table': 'configsettings_returnsettings',
            },
        ),
    ]
