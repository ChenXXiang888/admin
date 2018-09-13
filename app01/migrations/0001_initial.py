# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='外币货币名称')),
                ('rate', models.DecimalField(max_digits=10, decimal_places=3, verbose_name='汇率')),
            ],
            options={
                'verbose_name': '货币汇率表',
                'verbose_name_plural': '货币汇率表',
                'db_table': 'df_exchange_rate',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='商品名称')),
                ('image', models.ImageField(upload_to='app01/image/', verbose_name='商品图片')),
                ('desc', models.TextField(blank=True, default='', verbose_name='商品描述')),
                ('sale_price', models.IntegerField(default=0, verbose_name='售价')),
                ('agent_price', models.IntegerField(default=0, verbose_name='代理价')),
                ('cost_price', models.IntegerField(default=0, verbose_name='成本价')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('status', models.IntegerField(default=0, verbose_name='商品状态')),
                ('currency_id', models.IntegerField(default=0, verbose_name='货币id')),
            ],
            options={
                'verbose_name': '商品库商品',
                'verbose_name_plural': '商品库商品',
                'db_table': 'df_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='商品一级分类名称')),
                ('saler_uid', models.CharField(max_length=32, verbose_name='创建者uid')),
                ('status', models.IntegerField(default=0, verbose_name='一级分类状态')),
            ],
            options={
                'verbose_name': '商品商品一级分类',
                'verbose_name_plural': '商品商品一级分类',
                'db_table': 'df_goods_category',
            },
        ),
        migrations.CreateModel(
            name='GoodsLib',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='商品库名称')),
                ('saler_uid', models.CharField(max_length=32, verbose_name='创建者uid')),
                ('connect_lib', models.IntegerField(default=0, verbose_name='关联商品库')),
                ('status', models.IntegerField(default=0, verbose_name='商品库状态')),
                ('type', models.IntegerField(default=0, verbose_name='商品库类型')),
            ],
            options={
                'verbose_name': '商品库',
                'verbose_name_plural': '商品库',
                'db_table': 'df_goods_lib',
            },
        ),
        migrations.CreateModel(
            name='GoodsSecondCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='商品一级分类名称')),
                ('status', models.IntegerField(default=0, verbose_name='二级分类状态')),
                ('parent_id', models.ForeignKey(to='app01.GoodsCategory', verbose_name='一级分类id')),
            ],
            options={
                'verbose_name': '商品商品二级分类',
                'verbose_name_plural': '商品商品二级分类',
                'db_table': 'df_goods_second_category',
            },
        ),
        migrations.CreateModel(
            name='GoodsSku',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sku_name', models.CharField(max_length=32, verbose_name='商品规格名称')),
                ('sale_price', models.IntegerField(default=0, verbose_name='售价')),
                ('agent_price', models.IntegerField(default=0, verbose_name='代理价')),
                ('cost_price', models.IntegerField(default=0, verbose_name='成本价')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('status', models.IntegerField(default=0, verbose_name='商品规格状态')),
                ('goods_id', models.ForeignKey(to='app01.Goods', verbose_name='商品id')),
            ],
            options={
                'verbose_name': '商品规格表',
                'verbose_name_plural': '商品规格表',
                'db_table': 'df_goodssku',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category_id',
            field=models.ForeignKey(to='app01.GoodsCategory', verbose_name='一级分类id'),
        ),
        migrations.AddField(
            model_name='goods',
            name='currency_name',
            field=models.ForeignKey(to='app01.ExchangeRate', verbose_name='货币名称'),
        ),
        migrations.AddField(
            model_name='goods',
            name='lib_id',
            field=models.ForeignKey(to='app01.GoodsLib', verbose_name='商品库id'),
        ),
        migrations.AddField(
            model_name='goods',
            name='second_category_id',
            field=models.ForeignKey(to='app01.GoodsSecondCategory', verbose_name='二级分类id'),
        ),
    ]
