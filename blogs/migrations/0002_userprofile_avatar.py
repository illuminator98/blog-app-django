# Generated by Django 4.1.4 on 2023-01-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='blog_app/media/avatar.png', upload_to=''),
        ),
    ]
