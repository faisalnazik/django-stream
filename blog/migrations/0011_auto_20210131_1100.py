# Generated by Django 3.1.4 on 2021-01-31 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_tvshowdetails_tvshowparent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshowparent',
            name='parent',
        ),
        migrations.DeleteModel(
            name='TvShowDetails',
        ),
        migrations.DeleteModel(
            name='TvShowParent',
        ),
    ]
