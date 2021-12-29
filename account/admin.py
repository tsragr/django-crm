from django.contrib import admin
from account import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'avatar', 'first_name', 'second_name', 'patronymic')
    list_display_links = ('user',)
