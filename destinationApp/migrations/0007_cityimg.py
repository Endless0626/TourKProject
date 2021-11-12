# Generated by Django 2.2.4 on 2021-05-31 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinationApp', '0006_special_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='City/', verbose_name='城市照片')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cityImgs', to='destinationApp.City', verbose_name='城市')),
            ],
            options={
                'verbose_name': '城市图片',
                'verbose_name_plural': '城市图片',
            },
        ),
    ]
