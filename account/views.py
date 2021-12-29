from django.shortcuts import render
from django.contrib.auth import forms
from django.contrib.auth import views
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from account import models
from account.forms import ProfileForm


class SignUpView(generic.CreateView):
    """User registration class"""
    form_class = forms.UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return '/account/profile/'


class ProfileView(LoginRequiredMixin, generic.DetailView, generic.UpdateView):
    """
    User's profile view
    """
    login_url = '/account/login/'
    template_name = 'registration/profile.html'
    context_object_name = 'profile'
    form_class = ProfileForm

    def get_success_url(self):
        return '/account/profile/'

    def get_object(self, queryset=None):
        return models.Profile.objects.get_or_create(user=self.request.user)[0]
