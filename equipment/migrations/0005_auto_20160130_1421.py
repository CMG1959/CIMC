# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-30 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_auto_20160109_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentinfo',
            options={'verbose_name': 'Equipment - Information', 'verbose_name_plural': 'Equipment - Information'},
        ),
        migrations.AlterModelOptions(
            name='equipmentmanufacturer',
            options={'verbose_name': 'Equipment - Manufacturer', 'verbose_name_plural': 'Equipment - Manufacturers'},
        ),
        migrations.AlterModelOptions(
            name='equipmentpm',
            options={'verbose_name': 'Record - Performed PM', 'verbose_name_plural': 'Record - Performed PM'},
        ),
        migrations.AlterModelOptions(
            name='equipmentrepair',
            options={'verbose_name': 'Record - Equipment Repairs', 'verbose_name_plural': 'Record - Equipment Repairs'},
        ),
        migrations.AlterModelOptions(
            name='equipmenttype',
            options={'verbose_name': 'Equipment - Type', 'verbose_name_plural': 'Equipment - Types'},
        ),
        migrations.AlterModelOptions(
            name='pm',
            options={'verbose_name': 'Equipment - Preventative Maintenance Item', 'verbose_name_plural': 'Equipment - Preventative Maintenance Items'},
        ),
        migrations.AlterModelOptions(
            name='pmfreq',
            options={'verbose_name': 'Equipment - Preventative Maintenance Frequency', 'verbose_name_plural': 'Equipment - Preventative Maintenance Frequencies'},
        ),
        migrations.AlterField(
            model_name='equipmentpm',
            name='employee',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Employees', verbose_name=b'Technician'),
        ),
        migrations.AlterField(
            model_name='equipmentrepair',
            name='employee',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Employees', verbose_name=b'Technician'),
        ),
    ]
