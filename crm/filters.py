import django_filters
from crm import models


class CompanyFilter(django_filters.FilterSet):
    """
    Company's filter
    """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')
    division__name = django_filters.CharFilter(field_name='divisions__name', lookup_expr='icontains')

    class Meta:
        model = models.Company
        fields = ('name', 'city')


class PostFilter(django_filters.FilterSet):
    """
    Post's filter
    """
    salary = django_filters.NumberFilter()
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.Post
        fields = ('name', 'division', 'salary', 'salary__gt', 'salary__lt')


class EmployerFilter(django_filters.FilterSet):
    """
    Employer's filter
    """
    class Meta:
        model = models.Employer
        fields = ('post__division',)
