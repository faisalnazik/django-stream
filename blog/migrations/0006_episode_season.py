# Generated by Django 3.1.4 on 2021-01-29 08:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210129_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_slug', models.SlugField(max_length=250, unique_for_date='tv_show_publish')),
                ('season_publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('season_status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('season_views', models.IntegerField(default=0)),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season', to='blog.tv_show')),
            ],
            options={
                'ordering': ('-season_publish',),
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_Show_episode_link', models.CharField(max_length=1000, null=True)),
                ('episode_publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('episode_views', models.IntegerField(default=0)),
                ('episode_slug', models.SlugField(max_length=250, unique_for_date='tv_show_publish')),
                ('episode_status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('episode_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episode_number', to='blog.season')),
            ],
        ),
    ]
