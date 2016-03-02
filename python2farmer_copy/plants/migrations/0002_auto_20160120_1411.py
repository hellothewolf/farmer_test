# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='Content',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9   ', blank=True),
        ),
    ]
