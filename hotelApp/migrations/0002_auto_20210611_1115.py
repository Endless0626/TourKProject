# Generated by Django 2.2.4 on 2021-06-11 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotel',
            options={'ordering': ('-views',), 'verbose_name': '酒店', 'verbose_name_plural': '酒店'},
        ),
        migrations.DeleteModel(
            name='CommentImgs',
        ),
    ]
