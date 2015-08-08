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
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('receiver', models.EmailField(max_length=75, verbose_name='Email recipient')),
                ('submit', models.CharField(default='Submit', max_length=30, verbose_name='Submit button value')),
                ('success_message', models.TextField(default='Thank you for the message.', verbose_name='Success message')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
