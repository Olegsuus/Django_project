# Generated by Django 5.0.2 on 2024-02-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('text', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
