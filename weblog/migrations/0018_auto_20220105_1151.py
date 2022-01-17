# Generated by Django 3.2.9 on 2022-01-05 08:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0017_auto_20220105_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='child',
        ),
        migrations.AddField(
            model_name='comment',
            name='child',
            field=models.ManyToManyField(blank=True, null=True, related_name='_weblog_comment_child_+', to='weblog.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 8, 21, 59, 723091, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 8, 21, 59, 722093, tzinfo=utc)),
        ),
    ]
