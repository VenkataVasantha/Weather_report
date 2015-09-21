# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.PositiveSmallIntegerField(default=0)),
                ('zipimg', models.CharField(max_length=200)),
                ('ziptemp', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
    ]
