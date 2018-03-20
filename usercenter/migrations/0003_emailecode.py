# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0002_deivcevcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailEcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email', db_index=True)),
                ('ecode', models.CharField(max_length=64, verbose_name='ecode')),
            ],
        ),
    ]
