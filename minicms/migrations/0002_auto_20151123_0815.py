# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minicms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('position',)},
        ),
        migrations.AlterField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(related_name='children', blank=True, to='minicms.Page', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='position',
            field=models.PositiveIntegerField(default=1000),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('slug', 'parent')]),
        ),
    ]
