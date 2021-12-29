from django.db import models
from django.contrib.auth.models import User
from account.services import get_path_upload_avatar, validate_size_image
from django.core.validators import FileExtensionValidator


class Profile(models.Model):
    """Profile's model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    avatar = models.ImageField(upload_to=get_path_upload_avatar,
                               validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image],
                               blank=True,
                               null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Profile: {self.first_name} {self.second_name} {self.patronymic}"
