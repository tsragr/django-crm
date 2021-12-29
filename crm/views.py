from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from crm import forms
from crm import models
from crm import filters
from django.core.paginator import Paginator
from django.urls import reverse_lazy


class CreateCompanyView(LoginRequiredMixin, generic.CreateView):
    """
    View create company
    """
    form_class = forms.CompanyForms
    template_name = 'crm/create.html'
    success_url = '/crm/company_list/'
    login_url = '/account/login/'


class ListCompanyView(LoginRequiredMixin, generic.ListView):
    """
    View return lists of companies
    """
    login_url = '/account/login/'
    template_name = 'crm/company_list.html'
    queryset = models.Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.queryset
        filter = filters.CompanyFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context


class DeleteCompanyView(LoginRequiredMixin, generic.DeleteView):
    """
    View for delete company
    """
    template_name = 'crm/delete.html'
    success_url = '/crm/company_list/'
    model = models.Company
    login_url = '/account/login/'


class CreateDivisionView(LoginRequiredMixin, generic.CreateView):
    """
    View create division
    """
    form_class = forms.DivisionForms
    template_name = 'crm/create.html'
    login_url = '/account/login/'

    def get_success_url(self):
        return reverse_lazy('crm:dv-detail', kwargs={'pk': self.object.pk})


class DetailDivisionView(LoginRequiredMixin, generic.DetailView, generic.UpdateView):
    """
    View for retrieve division
    """
    login_url = '/account/login/'
    template_name = 'crm/detail_division.html'
    context_object_name = 'division'
    form_class = forms.DivisionForms

    def get_success_url(self):
        return reverse_lazy('crm:dv-detail', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return get_object_or_404(models.Division, pk=self.kwargs.get('pk'))


class DeleteDivisionView(LoginRequiredMixin, generic.DeleteView):
    """
    View for delete division
    """
    template_name = 'crm/delete.html'
    success_url = '/crm/company_list/'
    model = models.Division
    login_url = '/account/login/'


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    """
    View create post
    """
    form_class = forms.PostForms
    template_name = 'crm/create.html'
    login_url = '/account/login/'

    def get_success_url(self):
        return reverse_lazy('crm:dv-detail', kwargs={'pk': self.object.division.pk})


class ListPostView(LoginRequiredMixin, generic.ListView):
    """
    View return lists of posts
    """
    login_url = '/account/login/'
    template_name = 'crm/post_list.html'
    queryset = models.Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.queryset
        filter = filters.PostFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    """
    View for delete post
    """
    template_name = 'crm/delete.html'
    success_url = '/crm/company_list/'
    model = models.Post
    login_url = '/account/login/'


class CreateEmployerView(LoginRequiredMixin, generic.CreateView):
    """
    View create employer
    """
    form_class = forms.EmployerForms
    template_name = 'crm/create.html'
    login_url = '/account/login/'

    def get_success_url(self):
        return reverse_lazy('crm:ep-detail', kwargs={'pk': self.object.pk})


class DetailEmployerView(LoginRequiredMixin, generic.DetailView, generic.UpdateView):
    """
    View for retrieve employer
    """
    login_url = '/account/login/'
    template_name = 'crm/detail_employer.html'
    context_object_name = 'employer'
    form_class = forms.EmployerForms

    def get_success_url(self):
        return reverse_lazy('crm:ep-detail', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return get_object_or_404(models.Employer, pk=self.kwargs.get('pk'))


class ListEmployerView(LoginRequiredMixin, generic.ListView):
    """
    View return lists of employers
    """
    login_url = '/account/login/'
    template_name = 'crm/employer_list.html'
    queryset = models.Employer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.queryset
        filter = filters.EmployerFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context


class DeleteEmployerView(LoginRequiredMixin, generic.DeleteView):
    """
    View for delete employer
    """
    template_name = 'crm/delete.html'
    success_url = '/crm/company_list/'
    model = models.Employer
    login_url = '/account/login/'
