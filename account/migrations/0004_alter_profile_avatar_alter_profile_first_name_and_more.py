# Generated by Django 4.0 on 2021-12-23 13:06

import account.services
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=account.services.get_path_upload_avatar, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), account.services.validate_size_image]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
