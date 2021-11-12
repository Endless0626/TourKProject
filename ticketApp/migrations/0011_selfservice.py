# Generated by Django 2.2.4 on 2021-06-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0010_remove_ticket_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='selfService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.CharField(blank=True, max_length=50, null=True, verbose_name='自助值机时间')),
                ('Home', models.CharField(blank=True, max_length=100, null=True, verbose_name='航空公司官网')),
                ('Name', models.CharField(choices=[('大韩航空', '大韩航空'), ('韩亚航空', '韩亚航空'), ('山东航空', '山东航空'), ('青岛航空', '青岛航空'), ('春秋航空', '春秋航空'), ('釜山航空', '釜山航空'), ('中国南方航空', '中国南方航空'), ('真航空', '真航空'), ('中国国际航空', '中国国际航空'), ('中国东方航空', '中国东方航空'), ('济州航空', '济州航空')], max_length=10, verbose_name='航空公司')),
                ('Code', models.CharField(blank=True, max_length=5, null=True, verbose_name='航空公司代号')),
                ('Logo', models.ImageField(blank=True, upload_to='Airport/', verbose_name='航空公司标志')),
            ],
            options={
                'verbose_name': '航空公司信息',
                'verbose_name_plural': '航空公司信息',
            },
        ),
    ]