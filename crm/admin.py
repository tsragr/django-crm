from django.contrib import admin
from crm import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "city")
    list_display_links = ("name",)


@admin.register(models.Division)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "company", "city")
    list_display_links = ("name",)


@admin.register(models.Post)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "division", "salary")
    list_display_links = ("name",)


@admin.register(models.Employer)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "worker", "post", "date_employment")
    list_display_links = ("worker",)
