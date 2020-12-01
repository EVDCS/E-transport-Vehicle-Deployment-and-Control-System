# Generated by Django 3.1.3 on 2020-11-26 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201124_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.DeleteModel(
            name='rails',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='WorldBorder',
        ),
        migrations.RemoveField(
            model_name='assign_vehicle',
            name='route_id',
        ),
        migrations.AddField(
            model_name='assign_vehicle',
            name='destination',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assign_vehicle',
            name='length',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assign_vehicle',
            name='price',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assign_vehicle',
            name='source',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assign_vehicle',
            name='assign_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 440740), verbose_name='date assigned'),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 438711), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 431723), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 436716), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='machine_data',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 436716), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 431219), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='route',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 437713), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_type',
            field=models.CharField(default='normal', max_length=200),
        ),
        migrations.AlterField(
            model_name='routetypes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 437713)),
        ),
        migrations.AlterField(
            model_name='station',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 435718), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='subcity',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 432726), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 434721), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='vehicles_location',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 439746), verbose_name='date registerd'),
        ),
        migrations.AlterField(
            model_name='waiting_time',
            name='reg_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 10, 43, 3, 439746), verbose_name='date registerd'),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]