# Generated by Django 3.1.4 on 2021-01-29 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_episode_season_tv_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='number',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
    ]
