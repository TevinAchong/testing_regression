# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regressionApp', '0002_auto_20180412_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PredYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PrevPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PrevYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='cropprediction',
            name='predictedPriceOne',
        ),
        migrations.RemoveField(
            model_name='cropprediction',
            name='predictedPriceTwo',
        ),
        migrations.RemoveField(
            model_name='cropprediction',
            name='predictedYearOne',
        ),
        migrations.RemoveField(
            model_name='cropprediction',
            name='predictedYearTwo',
        ),
        migrations.AddField(
            model_name='cropprediction',
            name='predPrices',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='regressionApp.PredPrice'),
        ),
        migrations.AddField(
            model_name='cropprediction',
            name='predYears',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='regressionApp.PredYear'),
        ),
        migrations.AddField(
            model_name='cropprediction',
            name='prevPrices',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='regressionApp.PrevPrice'),
        ),
        migrations.AddField(
            model_name='cropprediction',
            name='prevYears',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='regressionApp.PrevYear'),
        ),
    ]
