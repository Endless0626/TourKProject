# Generated by Django 2.2.4 on 2021-06-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0008_auto_20210604_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='logo',
            field=models.ImageField(blank=True, upload_to='AirportLogo/', verbose_name='航空公司标志'),
        ),
    ]
