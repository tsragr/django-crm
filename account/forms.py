from account import models
from django import forms


class ProfileForm(forms.ModelForm):
    """
    Profile's form for user
    """
    class Meta:
        model = models.Profile
        exclude = ('user',)
