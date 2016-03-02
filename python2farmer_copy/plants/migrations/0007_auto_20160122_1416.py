# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0006_auto_20160120_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='intro_picture_path',
        ),
        migrations.AlterField(
            model_name='article',
            name='intro',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='intro', blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='path_picture',
            field=models.FilePathField(path='static/plantpicture/', max_length=256, verbose_name='\u690d\u7269\u56fe\u7247\u8def\u5f84'),
        ),
    ]
