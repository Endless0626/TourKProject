# Generated by Django 2.2.4 on 2021-06-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteApp', '0009_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='pagephoto',
            field=models.ImageField(blank=True, null=True, upload_to='note/', verbose_name='封面图'),
        ),
    ]
