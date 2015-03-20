# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20150320_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(unique=True, max_length=2, default='PL', choices=[('PL', 'Player'), ('TC', 'Team Captain'), ('MA', 'Manager'), ('AN', 'Analyst')]),
            preserve_default=True,
        ),
    ]
