from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='job_listing-index'),
]