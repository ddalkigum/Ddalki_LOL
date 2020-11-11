# Generated by Django 3.1.1 on 2020-09-24 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('champions', '0001_initial'),
        ('tips', '0002_tip_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='champion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tips', to='champions.champion'),
        ),
        migrations.AlterField(
            model_name='tip',
            name='nickname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tips', to=settings.AUTH_USER_MODEL),
        ),
    ]
