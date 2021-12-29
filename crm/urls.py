from django.urls import path
from crm import views

app_name = 'crm'

urlpatterns = [
    path('company_create/', views.CreateCompanyView.as_view(), name='cp-create'),
    path('company_list/', views.ListCompanyView.as_view(), name='cp-list'),
    path('company_delete/<int:pk>/', views.DeleteCompanyView.as_view(), name='cp-delete'),
    path('division_create/', views.CreateDivisionView.as_view(), name='dv-create'),
    path('division_detail/<int:pk>/', views.DetailDivisionView.as_view(), name='dv-detail'),
    path('division_delete/<int:pk>/', views.DeleteDivisionView.as_view(), name='dv-delete'),
    path('post_create/', views.CreatePostView.as_view(), name='ps-create'),
    path('post_list/', views.ListPostView.as_view(), name='ps-list'),
    path('employer_create/', views.CreateEmployerView.as_view(), name='ep-create'),
    path('employer_detail/<int:pk>/', views.DetailEmployerView.as_view(), name='ep-detail'),
    path('employer_list/', views.ListEmployerView.as_view(), name='ep-list'),
]
