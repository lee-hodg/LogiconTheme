# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 21:04
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0006_auto_20161012_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='contact_text',
            field=mezzanine.core.fields.RichTextField(default=b'One of our team would be happy to discuss in detail our skillset and experience and how we fit in with your project. Send us an email using the link below.', help_text=b'Text for contact section', max_length=200),
        ),
    ]
