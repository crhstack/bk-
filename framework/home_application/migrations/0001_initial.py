# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('param1', models.CharField(max_length=10, verbose_name='\u53c2\u65701')),
                ('param2', models.CharField(max_length=10, verbose_name='\u53c2\u65702')),
                ('result', models.CharField(max_length=10, verbose_name='\u7ed3\u679c')),
            ],
        ),
    ]
