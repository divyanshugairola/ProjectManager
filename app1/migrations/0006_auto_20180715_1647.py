# Generated by Django 2.0.1 on 2018-07-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20180715_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='date_of_submission',
            field=models.DateField(auto_now_add=True),
        ),
    ]