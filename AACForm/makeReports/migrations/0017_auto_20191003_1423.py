# Generated by Django 2.2.5 on 2019-10-03 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0016_auto_20191002_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentsupplement',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 10, 3, 14, 23, 13, 368164)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subassessment',
            name='proficient',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(default='Rubric 2019-10-03 14:22:51.895973', max_length=150),
        ),
        migrations.DeleteModel(
            name='SubassessmentData',
        ),
    ]
