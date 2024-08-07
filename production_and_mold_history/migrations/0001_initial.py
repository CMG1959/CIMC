# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 18:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceRequests',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True)),
                ('Requestor_Name', models.CharField(max_length=20, verbose_name=b'Requestor Name')),
                ('Request_Time', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Requested')),
                ('Request_Shift', models.SmallIntegerField(verbose_name=b'Shift')),
                ('Request_Loc', models.SmallIntegerField(verbose_name=b'Request Location')),
                ('Request_Source', models.SmallIntegerField(verbose_name=b'Request Location')),
                ('Tool_id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('Tool_Number', models.CharField(max_length=20, verbose_name=b'Tool Number')),
                ('Request_Desc', models.CharField(max_length=1000, verbose_name=b'Request Description')),
                ('Ack_Acknowledged', models.BooleanField(default=False, verbose_name=b'Ackknowledged')),
                ('Ack_Time', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Acknowledged')),
                ('Ack_Name', models.CharField(max_length=20, verbose_name=b'Acknowledger Name')),
                ('Ack_Notes', models.CharField(max_length=1000, verbose_name=b'Acknowledger Comments')),
                ('Ack_Link_WO', models.IntegerField(verbose_name=b'WO')),
            ],
            options={
                'verbose_name': 'Maintenance Requests',
                'managed': False,
                'verbose_name_plural': 'Maintenance Requests',
            },
        ),
        migrations.CreateModel(
            name='MoldHistory',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('parent_id', models.CharField(default=uuid.uuid4, editable=False, max_length=36)),
                ('Date_Performed', models.DateField(default=datetime.date.today, verbose_name=b'Date Performed')),
                ('inspectorName', models.CharField(blank=True, max_length=20, verbose_name=b'Name')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('moldNumber', models.CharField(max_length=12, verbose_name=b'Mold Number')),
                ('descEvent', models.CharField(blank=True, max_length=1000, null=True, verbose_name=b'Event Description')),
                ('pm', models.BooleanField(default=False, verbose_name=b'Preventative Maintenance')),
                ('repair', models.BooleanField(default=False, verbose_name=b'Repair')),
                ('hours_worked', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=b'Hours worked')),
                ('loc_id', models.SmallIntegerField(default=10, verbose_name=b'Location ID')),
            ],
            options={
                'verbose_name': 'Mold History Log Entry',
                'managed': False,
                'verbose_name_plural': 'Mold History Log Entries',
            },
        ),
        migrations.CreateModel(
            name='ProductionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('dateCreatedL', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created')),
                ('jobNumber', models.CharField(blank=True, max_length=20, verbose_name=b'Job Number')),
                ('descEvent', models.CharField(max_length=1000, verbose_name=b'Event Description')),
                ('Prod_shift', models.IntegerField(blank=True, null=True, verbose_name=b'Shift')),
                ('Prod_Date', models.DateField(blank=True, null=True, verbose_name=b'Short Date')),
                ('notifyToolroom', models.BooleanField(default=False, verbose_name=b'Notify toolroom')),
                ('STA_Reported', models.IntegerField(blank=True, default=0, verbose_name=b'Reported Workstation')),
            ],
            options={
                'verbose_name': 'Production History Log Entry',
                'managed': False,
                'verbose_name_plural': 'Production History Log Entries',
            },
        ),
    ]
