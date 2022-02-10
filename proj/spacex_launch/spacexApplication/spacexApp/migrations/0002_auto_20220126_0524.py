# Generated by Django 3.2.8 on 2022-01-26 05:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spacexApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='futurelaunch',
            name='description',
        ),
        migrations.RemoveField(
            model_name='futurelaunch',
            name='last_modified',
        ),
        migrations.AddField(
            model_name='futurelaunch',
            name='when',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
