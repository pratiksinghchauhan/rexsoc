# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161223_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('username', models.CharField(null=True, max_length=30)),
                ('firstname', models.CharField(null=True, max_length=30)),
                ('lastname', models.CharField(null=True, max_length=30)),
                ('public_email', models.EmailField(null=True, max_length=30)),
                ('url', models.TextField(null=True, validators=[django.core.validators.URLValidator()])),
                ('institution', models.CharField(null=True, max_length=30)),
                ('location', models.CharField(null=True, max_length=30)),
            ],
        ),
    ]
