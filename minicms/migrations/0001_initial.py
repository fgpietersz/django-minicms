# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.SlugField()),
                ('position', models.PositiveIntegerField()),
                ('urlpath', models.CharField(unique=True, max_length=1000, editable=False)),
                ('parent', models.ForeignKey(on_delete=models.PROTECT, related_name='children', to='minicms.Page', null=True)),
            ],
        ),
    ]
