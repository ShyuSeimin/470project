# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150715_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='stree',
        ),
    ]
