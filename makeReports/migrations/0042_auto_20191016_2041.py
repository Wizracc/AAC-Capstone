# Generated by Django 2.2.5 on 2019-10-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0041_auto_20191013_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessmentversion',
            name='firstInstance',
        ),
        migrations.RemoveField(
            model_name='sloinreport',
            name='firstInstance',
        ),
        migrations.AddField(
            model_name='assessment',
            name='numberOfUses',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='slo',
            name='numberOfUses',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='gradgoal',
            name='text',
            field=models.CharField(max_length=300),
        ),
    ]