# Generated by Django 2.2.4 on 2021-06-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='图片标题'),
        ),
    ]
