# Generated by Django 2.2.5 on 2019-10-09 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0028_auto_20191007_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='numberOfSLOs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sloinreport',
            name='number',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='gradedrubricitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeReports.RubricItem'),
        ),
    ]