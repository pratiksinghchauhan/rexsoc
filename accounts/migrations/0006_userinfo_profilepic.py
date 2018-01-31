# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20161224_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='profilepic',
            field=models.ImageField(default='http://www.sbesports.com/uploads/7/8/6/7/7867102/no-image_5_orig.png', upload_to=''),
        ),
    ]
