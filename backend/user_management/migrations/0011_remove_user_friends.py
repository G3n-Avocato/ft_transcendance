# Generated by Django 5.0.2 on 2024-03-11 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0010_user_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
    ]
