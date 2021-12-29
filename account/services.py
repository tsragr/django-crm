import os
from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """ Create path for user's avatar """
    return f'avatar/user_{instance.id}/{file}'


def validate_size_image(file_obj):
    """ Check file's size """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"File's size maximum is  {megabyte_limit}MB")

