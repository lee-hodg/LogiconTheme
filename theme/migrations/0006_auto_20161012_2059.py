# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0005_auto_20161012_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='contact_text',
            field=models.CharField(default=b'One of our team would be happy to discuss in detail our skillset and experience and how we fit in with your project. Send us an email using the link below.', help_text=b'Text for contact section', max_length=200),
        ),
    ]
