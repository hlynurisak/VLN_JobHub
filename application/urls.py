from django.urls import path
from . import views

urlpatterns = [
    path('application-info/<int:job_id>/', views.application_view, name='applications'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
]