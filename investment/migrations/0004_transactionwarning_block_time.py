# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0003_auto_20180419_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionwarning',
            name='block_time',
            field=models.DateTimeField(null=True, verbose_name='\u4ea4\u6613\u65f6\u95f4', blank=True),
        ),
    ]
