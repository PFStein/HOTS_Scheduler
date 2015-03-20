# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('player_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('end_time', models.DateTimeField(verbose_name='End Time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=2, default='PL', choices=[('PL', 'Player'), ('TC', 'Team Captain'), ('MA', 'Manager'), ('AN', 'Analyst')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('region', models.CharField(max_length=3, choices=[('USA', 'The United States'), ('EUR', 'Europe')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='registration',
            name='away_team',
            field=models.ForeignKey(to='scheduler.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registration',
            name='event',
            field=models.ForeignKey(to='scheduler.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='roles',
            field=models.ManyToManyField(to='scheduler.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='scheduler.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='hosting_team',
            field=models.ForeignKey(to='scheduler.Team'),
            preserve_default=True,
        ),
    ]
