# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20151109_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='externalView',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
