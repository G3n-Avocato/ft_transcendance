# Generated by Django 5.0.2 on 2024-04-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0016_user_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='', verbose_name='Select an image'),
        ),
    ]
