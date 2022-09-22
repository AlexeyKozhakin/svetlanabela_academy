# Generated by Django 4.0.4 on 2022-09-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_video_remove_lesson_video_lesson_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='videos',
        ),
        migrations.AddField(
            model_name='lesson',
            name='videos',
            field=models.ManyToManyField(null=True, related_name='videos', to='main.video'),
        ),
    ]
