# Generated by Django 2.0.1 on 2018-07-15 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Project'),
        ),
    ]
