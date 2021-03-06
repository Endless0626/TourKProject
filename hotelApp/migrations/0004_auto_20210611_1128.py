# Generated by Django 2.2.4 on 2021-06-11 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0003_commentimgs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercomment',
            options={'ordering': ('-commentDate',), 'verbose_name': '用户评价', 'verbose_name_plural': '用户评价'},
        ),
        migrations.AlterField(
            model_name='hotel',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='建成年份'),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='index',
            field=models.IntegerField(blank=True, null=True, verbose_name='评价指数'),
        ),
    ]
