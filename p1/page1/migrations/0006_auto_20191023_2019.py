# Generated by Django 2.2.5 on 2019-10-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0005_auto_20191023_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='workerprofile',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
        ),
    ]