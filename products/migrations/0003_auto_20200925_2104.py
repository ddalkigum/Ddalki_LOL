# Generated by Django 3.1.1 on 2020-09-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200925_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='horizontal',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vertical',
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.Meterial'),
        ),
    ]
