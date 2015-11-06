# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('videoDurationFe', models.CharField(max_length=255)),
                ('externalView', models.IntegerField()),
                ('dateCreate', models.DateTimeField()),
                ('licensedContent', models.BooleanField()),
                ('showHome', models.BooleanField()),
                ('category', models.ForeignKey(to='categories.Category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'data_post',
            },
        ),
    ]
