# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0002_auto_20150410_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseimmu',
            name='predecessor',
            field=models.ForeignKey(null=True, blank=True, to='planer.BaseImmu'),
        ),
    ]
