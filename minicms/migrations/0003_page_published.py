# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minicms', '0002_auto_20151123_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
