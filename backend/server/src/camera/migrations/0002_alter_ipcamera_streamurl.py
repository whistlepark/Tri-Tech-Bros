# Generated by Django 3.2.3 on 2021-05-29 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipcamera',
            name='streamURL',
            field=models.CharField(max_length=500),
        ),
    ]