# Generated by Django 2.2.5 on 2019-11-08 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makeReports', '0047_auto_20191106_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='decisionsactions',
            name='sloIR',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='makeReports.SLOInReport'),
        ),
        migrations.AddField(
            model_name='slostatus',
            name='sloIR',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='makeReports.SLOInReport'),
        ),
    ]