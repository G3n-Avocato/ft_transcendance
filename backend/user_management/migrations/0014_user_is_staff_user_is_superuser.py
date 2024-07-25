# Generated by Django 5.0.2 on 2024-03-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0013_friend_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]