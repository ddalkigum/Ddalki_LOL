# Generated by Django 3.1.1 on 2020-09-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('recommand', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
