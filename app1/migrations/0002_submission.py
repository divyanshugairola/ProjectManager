# Generated by Django 2.0.1 on 2018-07-15 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app1.Employee')),
                ('p_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.Project')),
            ],
        ),
    ]
