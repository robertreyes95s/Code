# Generated by Django 4.0.1 on 2022-02-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacexApp', '0005_alter_futurelaunch_launch_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futurelaunch',
            name='description',
            field=models.CharField(max_length=700),
        ),
    ]
