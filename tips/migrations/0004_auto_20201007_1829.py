# Generated by Django 3.1.2 on 2020-10-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0003_auto_20200924_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='recommand',
            field=models.IntegerField(null=True),
        ),
    ]
