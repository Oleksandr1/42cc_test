# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('last_name', models.CharField(max_length=256, verbose_name=b'Surname')),
                ('birthday', models.DateField(null=True, verbose_name=b'Data of Birth')),
                ('email', models.CharField(max_length=256, verbose_name=b'E-mail')),
                ('skype', models.CharField(max_length=256, verbose_name=b'skype')),
                ('jabber', models.CharField(max_length=256, verbose_name=b'Jabber/xmpp')),
                ('biography', models.TextField(verbose_name=b'Biography', blank=True)),
                ('other_contacts', models.TextField(verbose_name=b'other contacts', blank=True)),
            ],
        ),
    ]
