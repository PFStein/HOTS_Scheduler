# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='players',
        ),
        migrations.AddField(
            model_name='player',
            name='roles',
            field=models.ManyToManyField(to='teams.Role'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='region',
            field=models.CharField(choices=[('USA', 'The United States'), ('EUR', 'Europe')], max_length=3),
            preserve_default=True,
        ),
    ]
