# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateCreate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=255, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='externalView',
            field=models.IntegerField(default=0),
        ),
    ]
