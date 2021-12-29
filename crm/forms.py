from django import forms
from crm import models


class CompanyForms(forms.ModelForm):
    """
    Company's form
    """
    class Meta:
        model = models.Company
        fields = '__all__'


class DivisionForms(forms.ModelForm):
    """
    Division's form
    """
    class Meta:
        model = models.Division
        fields = '__all__'


class PostForms(forms.ModelForm):
    """
    Post's form
    """
    class Meta:
        model = models.Post
        fields = '__all__'


class EmployerForms(forms.ModelForm):
    """
    Employer's form
    """
    class Meta:
        model = models.Employer
        fields = '__all__'
