# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('slug', models.CharField(max_length=256, verbose_name='\u6240\u5c5e\u690d\u7269\u540d\u79f0\u62fc\u97f3')),
                ('author', models.CharField(max_length=256, null=True, verbose_name='\u4f5c\u8005', blank=True)),
                ('intro', models.TextField(default='', verbose_name='\u7b80\u4ecb', blank=True)),
                ('intro_picture_path', models.FilePathField(path='./plants/static/intropicture/', max_length=256, verbose_name='\u6587\u7ae0\u7b80\u4ecb\u56fe\u7247\u8def\u5f84')),
                ('content', models.TextField(default='', verbose_name='\u5185\u5bb9', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8868\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256, verbose_name='\u690d\u7269\u540d\u79f0')),
                ('slug', models.CharField(max_length=256, verbose_name='\u690d\u7269\u540d\u79f0\u62fc\u97f3', db_index=True)),
                ('path_picture', models.FilePathField(path='./plants/static/plantpicture/', max_length=256, verbose_name='\u690d\u7269\u56fe\u7247\u8def\u5f84')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u690d\u7269',
                'verbose_name_plural': '\u690d\u7269',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='belongtoplant',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u690d\u7269', to='plants.Plant'),
        ),
    ]
