# Generated by Django 3.1.4 on 2021-02-04 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0003_auto_20210204_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='tvshow',
            new_name='episode_parent',
        ),
    ]
