# Generated by Django 4.0.4 on 2022-09-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_lesson_videos_lesson_videos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_video_id',
            field=models.CharField(default='6vU7SzCdpuM', max_length=50),
            preserve_default=False,
        ),
    ]