# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('object_id', models.IntegerField(verbose_name='object_id')),
                ('title', models.CharField(max_length=512, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('desc', models.CharField(max_length=512, verbose_name='\u63cf\u8ff0')),
                ('is_read', models.BooleanField(default=False, db_index=True, verbose_name='\u5df2\u8bfb')),
                ('ntf_type', models.CharField(default=b'inner', max_length=64, verbose_name='\u6d88\u606f\u7c7b\u578b', db_index=True, choices=[(b'all', '\u7ad9\u5185\u4fe1+\u624b\u673a\u63a8\u9001'), (b'push', '\u624b\u673a\u63a8\u9001'), (b'inner', '\u7ad9\u5185\u4fe1')])),
                ('devicetype', models.CharField(default=b'all', max_length=64, verbose_name='\u8bbe\u5907\u7c7b\u578b', db_index=True, choices=[(b'all', '\u5168\u90e8'), (b'ANDROID', '\u5b89\u5353'), (b'iOS', '\u82f9\u679c')])),
                ('push_required', models.BooleanField(default=False, db_index=True, verbose_name='\u9700\u8981\u63a8\u9001')),
                ('push_datetime', models.DateTimeField(db_index=True, null=True, verbose_name='\u63a8\u9001\u65f6\u95f4', blank=True)),
                ('push_status', models.CharField(default=b'wait', max_length=16, verbose_name='\u63a8\u9001\u72b6\u6001', db_index=True, choices=[(b'wait', '\u7b49\u5f85\u53d1\u9001'), (b'send', '\u53d1\u9001\u4e2d'), (b'done', '\u53d1\u9001\u5b8c\u6210'), (b'fail', '\u53d1\u9001\u5931\u8d25'), (b'cancel', '\u53d6\u6d88\u53d1\u9001')])),
                ('message_id', models.CharField(max_length=256, null=True, verbose_name='Message', blank=True)),
                ('urlscheme', models.CharField(max_length=512, null=True, verbose_name='urlscheme', blank=True)),
                ('content_type', models.ForeignKey(verbose_name='\u7c7b\u578b', to='contenttypes.ContentType')),
                ('receiver', models.ForeignKey(verbose_name='\u6d88\u606f\u63a5\u6536\u8005', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-push_datetime',),
                'verbose_name': '\u901a\u77e5',
                'verbose_name_plural': '\u901a\u77e5',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('id', models.UUIDField(default=uuid.uuid1, serialize=False, editable=False, primary_key=True)),
                ('title', models.CharField(max_length=512, verbose_name='\u6807\u9898')),
                ('image', models.ImageField(help_text='1080x388', upload_to=b'message', null=True, verbose_name='\u5934\u56fe', blank=True)),
                ('summary', models.CharField(max_length=512, verbose_name='\u6982\u8981')),
                ('message_type', models.CharField(default=b'webview', max_length=32, verbose_name='\u7c7b\u578b', db_index=True, choices=[(b'webview', '\u5185\u90e8\u94fe\u63a5'), (b'browser', '\u5916\u90e8\u94fe\u63a5'), (b'article', '\u6587\u7ae0'), (b'app', 'app\u9996\u9875'), (b'message', '\u6d88\u606f\u5217\u8868')])),
                ('type_link', models.URLField(max_length=512, null=True, verbose_name='\u94fe\u63a5', blank=True)),
                ('type_id', models.CharField(max_length=64, null=True, verbose_name='Id', blank=True)),
                ('expired_datetime', models.DateTimeField(verbose_name='\u8fc7\u671f\u65f6\u95f4')),
                ('post_datetime', models.DateTimeField(null=True, verbose_name='\u5b9a\u65f6\u53d1\u5e03', blank=True)),
                ('post_topic', models.CharField(default=b'all', choices=[(b'all', '\u6240\u6709\u7528\u6237'), (b'login', '\u767b\u5f55\u7528\u6237'), (b'anonymous', '\u672a\u767b\u5f55\u7528\u6237'), (b'ios', 'ios\u6d4b\u8bd5'), (b'aliyun_test', '\u963f\u91cc\u4e91\u6d4b\u8bd5'), (b'xinshui_test', '\u6d4b\u8bd5')], max_length=64, blank=True, null=True, verbose_name='\u53d1\u9001\u7ed9\u9891\u9053', db_index=True)),
                ('post_method', models.CharField(default=b'all', max_length=64, verbose_name='\u53d1\u9001\u9014\u5f84', db_index=True, choices=[(b'all', '\u7ad9\u5185\u4fe1+\u624b\u673a\u63a8\u9001'), (b'push', '\u624b\u673a\u63a8\u9001'), (b'inner', '\u7ad9\u5185\u4fe1')])),
                ('devicetype', models.CharField(default=b'all', max_length=64, verbose_name='\u8bbe\u5907\u7c7b\u578b', db_index=True, choices=[(b'all', '\u5168\u90e8'), (b'ANDROID', '\u5b89\u5353'), (b'iOS', '\u82f9\u679c')])),
                ('status', models.CharField(default=b'0', max_length=16, verbose_name='\u72b6\u6001', db_index=True, choices=[(b'0', '\u8349\u7a3f'), (b'1', '\u53d1\u5e03')])),
                ('post_count', models.IntegerField(default=0, verbose_name='\u53d1\u9001\u4eba\u6570')),
                ('post_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, max_length=512, verbose_name='\u53d1\u9001\u7ed9\u7528\u6237', blank=True)),
            ],
            options={
                'ordering': ('-modified_datetime', '-post_datetime'),
                'verbose_name': '\u5e73\u53f0\u6d88\u606f',
                'verbose_name_plural': '\u5e73\u53f0\u6d88\u606f',
            },
        ),
        migrations.CreateModel(
            name='UserRead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('device', models.CharField(max_length=128, null=True, db_index=True)),
                ('notification', models.ForeignKey(to='notification.Notification')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified_datetime',),
                'abstract': False,
            },
        ),
    ]
