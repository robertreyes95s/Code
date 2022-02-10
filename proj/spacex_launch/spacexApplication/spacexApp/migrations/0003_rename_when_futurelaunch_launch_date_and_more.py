# Generated by Django 4.0.1 on 2022-02-06 03:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spacexApp', '0002_auto_20220126_0524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='futurelaunch',
            old_name='when',
            new_name='launch_date',
        ),
        migrations.AddField(
            model_name='futurelaunch',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='futurelaunch',
            name='launch_site',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
