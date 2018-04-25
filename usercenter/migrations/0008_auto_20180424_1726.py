# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0007_subscribe_coin_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBalanceRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('trans_type', models.CharField(default=b'invitation', max_length=16, verbose_name='\u4ea4\u6613\u7c7b\u578b', db_index=True, choices=[(b'invitation', b'\xe9\x82\x80\xe8\xaf\xb7\xe6\xb3\xa8\xe5\x86\x8c'), (b'register', b'\xe6\xb3\xa8\xe5\x86\x8c')])),
                ('amount', models.DecimalField(default=0.0, verbose_name='\u6570\u91cf', max_digits=20, decimal_places=9)),
            ],
            options={
                'ordering': ('-created_datetime',),
                'verbose_name': '\u7528\u6237\u4f59\u989d\u8bb0\u5f55',
                'verbose_name_plural': '\u7528\u6237\u4f59\u989d\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('code', models.CharField(unique=True, max_length=4, verbose_name='\u9080\u8bf7\u7801', db_index=True)),
                ('link_code', models.CharField(unique=True, max_length=8, verbose_name='\u94fe\u63a5\u7801', db_index=True)),
                ('link', models.URLField(verbose_name='\u9080\u8bf7\u94fe\u63a5')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u9080\u8bf7\u7801',
                'verbose_name_plural': '\u7528\u6237\u9080\u8bf7\u7801',
            },
        ),
        migrations.CreateModel(
            name='UserInvitationRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u9080\u8bf7\u8bb0\u5f55',
                'verbose_name_plural': '\u7528\u6237\u9080\u8bf7\u8bb0\u5f55',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(default=0.0, verbose_name='\u4f59\u989d', max_digits=20, decimal_places=9),
        ),
        migrations.AlterField(
            model_name='memberservice',
            name='price',
            field=models.DecimalField(default=0.0, verbose_name='\u91d1\u989d', max_digits=20, decimal_places=9),
        ),
        migrations.AddField(
            model_name='userinvitationrecord',
            name='inviter',
            field=models.ForeignKey(related_name='invite_users', verbose_name='\u9080\u8bf7\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='userinvitationrecord',
            name='user',
            field=models.ForeignKey(related_name='inviter', verbose_name='\u6ce8\u518c\u7528\u6237', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usercode',
            name='user',
            field=models.OneToOneField(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userbalancerecord',
            name='inviter',
            field=models.ForeignKey(related_name='inviter_banlance', verbose_name='\u88ab\u9080\u8bf7\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='userbalancerecord',
            name='user',
            field=models.ForeignKey(related_name='invite_users_banlance', verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL),
        ),
    ]
