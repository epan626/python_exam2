# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regandlogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fave', models.ManyToManyField(related_name='user_fave', to='regandlogin.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_quote', to='regandlogin.User')),
            ],
        ),
    ]