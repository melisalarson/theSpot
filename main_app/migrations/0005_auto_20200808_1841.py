# Generated by Django 3.1 on 2020-08-08 18:41

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200807_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='default_picture',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/uploads/', location='/Users/larson/sei/projects/projectwayfarer/theSpot/media/uploads/'), upload_to='uploads/'),
        ),
    ]
