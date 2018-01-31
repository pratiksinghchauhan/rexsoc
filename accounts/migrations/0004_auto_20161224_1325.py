# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewtable',
            options={'ordering': ['date']},
        ),
    ]
