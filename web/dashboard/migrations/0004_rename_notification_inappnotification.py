# Generated by Django 3.2.23 on 2024-08-30 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20240830_0135'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='InAppNotification',
        ),
    ]
