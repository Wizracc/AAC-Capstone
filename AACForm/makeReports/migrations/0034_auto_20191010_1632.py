# Generated by Django 2.2.5 on 2019-10-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0033_auto_20191009_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='decisionsactions',
            name='text',
            field=models.CharField(blank=True, default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='rubricitem',
            name='abbreviation',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='decisionsactions',
            name='actionTimeline',
            field=models.CharField(blank=True, default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='decisionsactions',
            name='dataUsed',
            field=models.CharField(blank=True, default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='decisionsactions',
            name='decisionMakers',
            field=models.CharField(blank=True, default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='decisionsactions',
            name='decisionProcess',
            field=models.CharField(blank=True, default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='decisionsactions',
            name='decisionTimeline',
            field=models.CharField(blank=True, default='', max_length=3000),
        ),
    ]