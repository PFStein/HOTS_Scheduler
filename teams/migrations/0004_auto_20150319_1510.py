# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_event_registrations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrations',
            old_name='team',
            new_name='away_team',
        ),
    ]
