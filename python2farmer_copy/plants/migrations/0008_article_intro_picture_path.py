# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_auto_20160122_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='intro_picture_path',
            field=models.FilePathField(default=datetime.datetime(2016, 1, 23, 7, 21, 35, 97265, tzinfo=utc), path='uploads/images/', max_length=256, verbose_name='\u6587\u7ae0\u7b80\u4ecb\u56fe\u7247\u8def\u5f84'),
            preserve_default=False,
        ),
    ]
