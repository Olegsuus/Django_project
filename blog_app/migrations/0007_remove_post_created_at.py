# Generated by Django 5.0.2 on 2024-02-17 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_post_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
    ]