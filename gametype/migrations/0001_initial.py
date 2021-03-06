# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 06:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gametypes', to='provider.Provider')),
            ],
            options={
                'db_table': 'gametype_gametype',
            },
        ),
    ]
