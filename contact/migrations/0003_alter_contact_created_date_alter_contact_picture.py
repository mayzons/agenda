# Generated by Django 5.1.7 on 2025-03-22 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_frist_name_contact_first_name_contact_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 22, 14, 31, 6, 951296, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(default=True, upload_to='pictures/%Y/%m/'),
        ),
    ]
