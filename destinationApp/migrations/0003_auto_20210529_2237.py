# Generated by Django 2.2.4 on 2021-05-29 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinationApp', '0002_auto_20210529_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='special',
            old_name='productType',
            new_name='specialType',
        ),
    ]
