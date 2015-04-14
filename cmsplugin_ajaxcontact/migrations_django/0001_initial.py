# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', primary_key=True, parent_link=True, auto_created=True, serialize=False)),
                ('receiver', models.EmailField(verbose_name='Email recipient', max_length=75)),
                ('submit', models.CharField(verbose_name='Submit button value', max_length=30, default='Submit')),
                ('success_message', models.TextField(verbose_name='Success message', default='Thank you for the message.')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
