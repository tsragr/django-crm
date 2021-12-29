from django.db import models
from account.models import Profile
from django.shortcuts import reverse
from datetime import date


class Company(models.Model):
    """
    Company's model
    """
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

    @property
    def list_divisions(self):
        return self.divisions.all()


class Division(models.Model):
    """
    Division's model
    """
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='divisions')

    def __str__(self):
        return f'{self.company.name}: {self.name}'

    def get_absolute_url(self):
        return reverse('crm:dv-detail', kwargs={'pk': self.id})

    @property
    def list_post(self):
        return self.posts.all()


class Post(models.Model):
    """
    Post's model
    """
    name = models.CharField(max_length=128)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='posts')
    salary = models.PositiveIntegerField()
    if_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.division.name} - {self.name}"


class Employer(models.Model):
    """
    Employer's model
    """
    worker = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='work')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='employer')
    date_employment = models.DateField(auto_now_add=True)
    date_new_employment = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.worker.first_name} - {self.post.name}"

    @property
    def time_on_work(self):
        if not self.date_new_employment:
            return date.today() - self.date_employment
        else:
            return date.today() - self.date_new_employment

    def get_absolute_url(self):
        return reverse('crm:ep-detail', kwargs={'pk': self.id})
