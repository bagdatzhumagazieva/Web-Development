# Generated by Django 2.2 on 2019-04-21 11:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20190405_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 21, 17, 40, 0, 447658)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 21, 17, 40, 0, 447658)),
        ),
    ]