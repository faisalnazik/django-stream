# Generated by Django 3.1.4 on 2021-02-04 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows', '0002_auto_20210204_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tvshow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvshows.tvshow'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='tvshow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvshows.tvshow'),
        ),
        migrations.DeleteModel(
            name='Season',
        ),
    ]
