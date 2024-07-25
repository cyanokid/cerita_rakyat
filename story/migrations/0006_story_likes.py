# Generated by Django 5.0.7 on 2024-07-21 23:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_profile_profile_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='story_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
