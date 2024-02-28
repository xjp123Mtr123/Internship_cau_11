# Generated by Django 3.2.15 on 2024-02-25 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_wx_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('purchase_time', models.DateTimeField(auto_now_add=True, verbose_name='进货时间')),
                ('category', models.CharField(max_length=50, verbose_name='商品类别')),
                ('product_name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('quantity', models.IntegerField(verbose_name='商品数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
            ],
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('category', models.CharField(max_length=50, verbose_name='商品类别')),
                ('product_name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('quantity', models.IntegerField(verbose_name='商品数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
            ],
        ),
    ]
