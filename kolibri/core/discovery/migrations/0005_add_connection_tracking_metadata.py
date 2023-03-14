# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-02-15 20:55
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("discovery", "0004_str_default_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="networklocation",
            name="broadcast_id",
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
        migrations.AddField(
            model_name="networklocation",
            name="connection_faults",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="networklocation",
            name="connection_status",
            field=models.CharField(
                choices=[
                    ("Conflict", "Conflict"),
                    ("ConnectionFailure", "ConnectionFailure"),
                    ("InvalidResponse", "InvalidResponse"),
                    ("Okay", "Okay"),
                    ("ResponseFailure", "ResponseFailure"),
                    ("ResponseTimeout", "ResponseTimeout"),
                    ("Unknown", "Unknown"),
                ],
                default="Unknown",
                max_length=32,
            ),
        ),
        migrations.AddField(
            model_name="networklocation",
            name="last_known_ip",
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]