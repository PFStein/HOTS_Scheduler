# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='roles',
            field=models.ManyToManyField(to='scheduler.Role', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='scheduler.Team', null=True),
            preserve_default=True,
        ),
    ]
