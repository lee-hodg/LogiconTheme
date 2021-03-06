# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0009_auto_20161013_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('zind', models.IntegerField(help_text=b'z-index in relation to other places.')),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
