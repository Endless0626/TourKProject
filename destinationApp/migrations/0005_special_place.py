# Generated by Django 2.2.4 on 2021-05-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinationApp', '0004_auto_20210529_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='place',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='所处城市'),
        ),
    ]
