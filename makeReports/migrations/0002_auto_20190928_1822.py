# Generated by Django 2.2.5 on 2019-09-28 23:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sloinreport',
            name='changedFromPrior',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sloinreport',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 28, 18, 22, 15, 5314)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sloinreport',
            name='firstInstance',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sloinreport',
            name='goalText',
            field=models.CharField(default='', max_length=600),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='degreeprogram',
            name='level',
            field=models.CharField(choices=[('UG', 'Undergraduate'), ('GR', 'Graduate')], max_length=75),
        ),
        migrations.AlterField(
            model_name='sloinreport',
            name='slo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeReports.SLO'),
        ),
        migrations.DeleteModel(
            name='SLOText',
        ),
    ]