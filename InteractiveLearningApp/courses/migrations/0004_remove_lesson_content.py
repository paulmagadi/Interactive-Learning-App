# Generated by Django 5.0.7 on 2024-07-22 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_content_quiz_data_remove_content_video_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='content',
        ),
    ]
