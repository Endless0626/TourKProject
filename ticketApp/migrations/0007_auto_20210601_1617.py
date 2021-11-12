# Generated by Django 2.2.4 on 2021-06-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0006_ticketimg_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketimg',
            name='Name',
            field=models.CharField(choices=[('大韩航空', '大韩航空'), ('韩亚航空', '韩亚航空'), ('山东航空', '山东航空'), ('青岛航空', '青岛航空'), ('春秋航空', '春秋航空'), ('釜山航空', '釜山航空'), ('中国南方航空', '中国南方航空'), ('真航空', '真航空'), ('中国国际航空', '中国国际航空'), ('中国东方航空', '中国东方航空'), ('济州航空', '济州航空')], max_length=10, verbose_name='航空公司'),
        ),
    ]