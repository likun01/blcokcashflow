# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_member', models.BooleanField(default=False, verbose_name='\u662f\u5426\u4f1a\u5458')),
                ('member_last_date', models.DateField(null=True, verbose_name='\u4f1a\u5458\u5230\u671f', blank=True)),
                ('token', models.CharField(max_length=64, verbose_name='token', db_index=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MemberOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('order_id', models.CharField(max_length=64, verbose_name='\u8ba2\u5355\u53f7', db_index=True)),
                ('guid', models.CharField(max_length=128, verbose_name='guid', db_index=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_date', models.DateField(verbose_name='\u622a\u6b62\u65f6\u95f4')),
                ('coin_type', models.CharField(db_index=True, max_length=32, verbose_name='\u5e01\u79cd', choices=[(b'BTC', b'BTC'), (b'BCH', b'BCH'), (b'ETH', b'ETH'), (b'LTC', b'LTC')])),
                ('coin_amount', models.DecimalField(default=0.0, verbose_name='\u865a\u62df\u5e01\u6570\u91cf', max_digits=20, decimal_places=9)),
                ('status', models.CharField(db_index=True, max_length=32, verbose_name='\u72b6\u6001', choices=[(b'new', b'new'), (b'paid', b'paid'), (b'confirmed', b'confirmed'), (b'complete', b'complete'), (b'expired', b'expired'), (b'invalid', b'invalid')])),
                ('exception_status', models.CharField(max_length=32, verbose_name='\u5f02\u5e38\u72b6\u6001', choices=[(b'false', b'false'), (b'paidPartial', b'paidPartial'), (b'paidOver', b'paidOver'), (b'paidLate', b'paidLate')])),
                ('invoice_id', models.CharField(max_length=64, verbose_name='\u4ea4\u6613id', db_index=True)),
                ('addresses', jsonfield.fields.JSONField(default=dict, verbose_name='\u4ea4\u6613\u5730\u5740')),
                ('origin', jsonfield.fields.JSONField(default=dict, verbose_name='\u539f\u59cb\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u8d2d\u4e70\u8ba2\u5355',
                'verbose_name_plural': '\u8d2d\u4e70\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='MemberOrderNotificationRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('invoice_id', models.CharField(max_length=64, verbose_name='\u4ea4\u6613id', db_index=True)),
                ('origin', jsonfield.fields.JSONField(default=dict, verbose_name='\u539f\u59cb\u4fe1\u606f')),
                ('status', models.CharField(db_index=True, max_length=32, verbose_name='\u72b6\u6001', choices=[(b'new', b'new'), (b'paid', b'paid'), (b'confirmed', b'confirmed'), (b'complete', b'complete'), (b'expired', b'expired'), (b'invalid', b'invalid')])),
                ('exception_status', models.CharField(max_length=32, verbose_name='\u5f02\u5e38\u72b6\u6001', choices=[(b'false', b'false'), (b'paidPartial', b'paidPartial'), (b'paidOver', b'paidOver'), (b'paidLate', b'paidLate')])),
                ('order', models.ForeignKey(verbose_name='\u8d2d\u4e70\u8ba2\u5355', to='usercenter.MemberOrder')),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u901a\u77e5\u8bb0\u5f55',
                'verbose_name_plural': '\u8ba2\u5355\u901a\u77e5\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='MemberService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('status', models.PositiveIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(1, '\u6709\u6548'), (0, '\u65e0\u6548')])),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('coin_type', models.CharField(db_index=True, max_length=32, verbose_name='\u5e01\u79cd', choices=[(b'BTC', b'BTC'), (b'BCH', b'BCH'), (b'ETH', b'ETH'), (b'LTC', b'LTC')])),
                ('duration', models.SmallIntegerField(default=0, verbose_name='\u65f6\u957f')),
                ('price', models.DecimalField(default=0.0, verbose_name='\u91d1\u989d', max_digits=8, decimal_places=2)),
                ('discount', models.SmallIntegerField(default=10, verbose_name='\u6298\u6263')),
            ],
            options={
                'verbose_name': '\u4f1a\u5458\u670d\u52a1',
                'verbose_name_plural': '\u4f1a\u5458\u670d\u52a1',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('status', models.PositiveIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(1, '\u6709\u6548'), (0, '\u65e0\u6548')])),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8ba2\u9605\u5217\u8868',
                'verbose_name_plural': '\u8ba2\u9605\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='SubscribeSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modified_datetime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('status', models.PositiveIntegerField(default=1, db_index=True, verbose_name='\u72b6\u6001', choices=[(1, '\u6709\u6548'), (0, '\u65e0\u6548')])),
                ('start_time', models.TimeField(default=b'00:00', verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.TimeField(default=b'23:59', verbose_name='\u622a\u6b62\u65f6\u95f4')),
                ('user', models.OneToOneField(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u8ba2\u9605\u8bbe\u7f6e',
                'verbose_name_plural': '\u8ba2\u9605\u8bbe\u7f6e',
            },
        ),
        migrations.AddField(
            model_name='memberorder',
            name='service',
            field=models.ForeignKey(verbose_name='\u8d2d\u4e70\u670d\u52a1', to='usercenter.MemberService'),
        ),
        migrations.AddField(
            model_name='memberorder',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL),
        ),
    ]
