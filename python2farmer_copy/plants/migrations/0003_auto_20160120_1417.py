# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20160120_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Content',
            new_name='content',
        ),
    ]
