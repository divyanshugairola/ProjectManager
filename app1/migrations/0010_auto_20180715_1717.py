# Generated by Django 2.0.1 on 2018-07-15 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20180715_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='subm_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 7, 15, 17, 17, 3, 536343)),
        ),
        migrations.AlterField(
            model_name='submission',
            name='date_of_submission',
            field=models.DateField(blank=True, null=True),
        ),
    ]