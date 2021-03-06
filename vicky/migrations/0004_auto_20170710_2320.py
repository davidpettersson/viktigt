# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vicky', '0003_auto_20170710_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='last_seen',
            new_name='message_last_presented',
        ),
        migrations.RenameField(
            model_name='alert',
            old_name='received',
            new_name='message_received',
        ),
        migrations.AddField(
            model_name='alert',
            name='message_sha1sum',
            field=models.CharField(default='0000000000000000', max_length=16),
            preserve_default=False,
        ),
    ]
