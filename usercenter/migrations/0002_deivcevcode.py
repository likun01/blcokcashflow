# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeivceVcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device', models.CharField(max_length=64, verbose_name='device', db_index=True)),
                ('vcode', models.CharField(max_length=64, verbose_name='vcode')),
            ],
        ),
    ]
