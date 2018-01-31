# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_userinfo_profilepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fromuser', models.ForeignKey(related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('touser', models.ForeignKey(related_name='getsfollowed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='firstname',
            field=models.CharField(null=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='institution',
            field=models.CharField(null=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastname',
            field=models.CharField(null=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.CharField(null=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='public_email',
            field=models.EmailField(null=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='url',
            field=models.TextField(null=True, default='', validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(null=True, default='', max_length=30),
        ),
    ]
