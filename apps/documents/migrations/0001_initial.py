# Generated by Django 2.2 on 2020-03-27 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='change_into',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '转入分析',
                'verbose_name_plural': '转入分析',
                'db_table': 'change_into',
            },
        ),
        migrations.CreateModel(
            name='change_out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '转出分析',
                'verbose_name_plural': '转出分析',
                'db_table': 'change_out',
            },
        ),
        migrations.CreateModel(
            name='Quotation_goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='单价')),
                ('meno', models.CharField(max_length=64, verbose_name='备注')),
            ],
            options={
                'verbose_name': '报价单',
                'verbose_name_plural': '报价单',
            },
        ),
        migrations.CreateModel(
            name='Quotation_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('qid', models.CharField(max_length=24, unique=True, verbose_name='单据编号')),
                ('meno', models.TextField(max_length=256, verbose_name='备注信息')),
            ],
            options={
                'verbose_name': '报价单',
                'verbose_name_plural': '报价单',
            },
        ),
    ]
