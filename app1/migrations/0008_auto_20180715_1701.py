# Generated by Django 2.0.1 on 2018-07-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20180715_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='subm_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]