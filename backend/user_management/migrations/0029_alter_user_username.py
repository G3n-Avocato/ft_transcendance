# Generated by Django 5.0.2 on 2024-06-06 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0028_match_rival'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
