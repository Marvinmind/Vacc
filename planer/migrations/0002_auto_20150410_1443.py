# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseimmu',
            name='predecessor',
            field=models.ForeignKey(null=True, to='planer.BaseImmu'),
        ),
    ]
