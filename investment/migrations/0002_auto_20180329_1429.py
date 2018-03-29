# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionWarning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('change', models.CharField(max_length=14, verbose_name='\u6da8\u8dcc', choices=[(b'up', '\u4e0a\u6da8'), (b'down', '\u4e0b\u8dcc')])),
                ('percent', models.IntegerField(default=0, verbose_name='\u767e\u5206\u4e4b')),
                ('pushed', models.BooleanField(default=False, verbose_name='\u5df2\u63a8\u9001')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6301\u4ed3\u9884\u8b66',
                'verbose_name_plural': '\u6301\u4ed3\u9884\u8b66',
            },
        ),
        migrations.CreateModel(
            name='TransactionWarning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('address', models.CharField(max_length=64, db_index=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=10)),
                ('pushed', models.BooleanField(default=False, verbose_name='\u5df2\u63a8\u9001')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u4ea4\u6613\u9884\u8b66',
                'verbose_name_plural': '\u4ea4\u6613\u9884\u8b66',
            },
        ),
        migrations.RemoveField(
            model_name='positionsubscribe',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transactionsubscribe',
            name='user',
        ),
        migrations.DeleteModel(
            name='PositionSubscribe',
        ),
        migrations.DeleteModel(
            name='TransactionSubscribe',
        ),
    ]
