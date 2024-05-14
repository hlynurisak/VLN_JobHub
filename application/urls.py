from django.urls import path
from . import views

urlpatterns = [
    path('applications/<int:job_id>/', views.application_view, name='applications'),
]