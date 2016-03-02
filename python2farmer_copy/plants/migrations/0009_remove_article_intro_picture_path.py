# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0008_article_intro_picture_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='intro_picture_path',
        ),
    ]
