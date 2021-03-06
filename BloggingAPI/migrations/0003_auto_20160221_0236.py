# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 02:36
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BloggingAPI', '0002_auto_20160220_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('contentType', models.CharField(default=b'text/plain', max_length=255)),
                ('comment', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='author_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.AddField(
            model_name='author',
            name='github',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='author',
            name='url',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=255), default=None, size=None),
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='contentType',
            field=models.CharField(default=b'text/plain', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='count',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='origin',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[(b'PUBLIC', b'PUBLIC'), (b'FOAF', b'FOAF'), (b'FRIENDS', b'FRIENDS'), (b'PRIVATE', b'PRIVATE'), (b'SERVERONLY', b'SERVERONLY')], default=b'PUBLIC', max_length=255),
        ),
        migrations.AlterField(
            model_name='author',
            name='host',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_img',
            field=models.ImageField(default=None, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to=b''),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BloggingAPI.Author'),
        ),
    ]
