# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regressionApp', '0004_auto_20180413_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropprediction',
            name='predPrices',
        ),
        migrations.AddField(
            model_name='cropprediction',
            name='predPrices',
            field=models.ManyToManyField(default=1, to='regressionApp.PredPrice'),
        ),
        migrations.RemoveField(
            model_name='cropprediction',
            name='predYears',
        ),
        migrations.AddField(
            model_name='cropprediction',
            name='predYears',
            field=models.ManyToManyField(default=1, related_name='predYears_set', to='regressionApp.PredYear'),
        ),
        migrations.RemoveField(
            model_name='cropprediction',
            name='prevPrices',
        ),
        migrations.AddField(
            model_name='cropprediction',
            name='prevPrices',
            field=models.ManyToManyField(default=1, to='regressionApp.PrevPrice'),
        ),
        migrations.RemoveField(
            model_name='cropprediction',
            name='prevYears',
        ),
        migrations.AddField(
            model_name='cropprediction',
            name='prevYears',
            field=models.ManyToManyField(default=1, to='regressionApp.PrevYear'),
        ),
    ]
