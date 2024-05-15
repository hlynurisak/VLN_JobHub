from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='company-index'),
    path('company-info/<int:company_id>/', views.company_info, name='company-info'),
]