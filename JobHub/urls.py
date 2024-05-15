from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage-index'),
    path('create_joblisting', views.create_joblisting, name='create_joblisting'),
]