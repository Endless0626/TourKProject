# Generated by Django 2.2.4 on 2021-05-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinationApp', '0007_cityimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='views',
            field=models.PositiveIntegerField(default=100, verbose_name='浏览量'),
        ),
    ]