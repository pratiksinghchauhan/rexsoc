# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewtable',
            name='date',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 12, 23, 7, 34, 11, 948599, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviewtable',
            name='user',
            field=models.CharField(max_length=30, default=datetime.datetime(2016, 12, 23, 7, 34, 36, 214621, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
