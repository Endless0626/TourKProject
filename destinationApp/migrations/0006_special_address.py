# Generated by Django 2.2.4 on 2021-05-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinationApp', '0005_special_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='具体地址'),
        ),
    ]
