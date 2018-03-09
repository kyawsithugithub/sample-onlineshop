# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 01:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandyname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('discountprice', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
                ('img1', models.FileField(upload_to='uploads/')),
                ('img2', models.FileField(upload_to='uploads/')),
                ('updatedate', models.DateField()),
                ('brandid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.brand')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineapp.category')),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]