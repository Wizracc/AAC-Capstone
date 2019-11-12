# Generated by Django 2.2.5 on 2019-10-06 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0024_merge_20191005_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessmentdata',
            name='dataBegin',
        ),
        migrations.RemoveField(
            model_name='assessmentdata',
            name='dataEnd',
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
            field=models.CharField(default='Rubric', max_length=150),
        ),
        migrations.DeleteModel(
            name='SubassessmentData',
        ),
    ]