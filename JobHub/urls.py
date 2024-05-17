from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage-index'),
    path('job/<int:id>/', views.get_job_by_id, name='get_job_by_id'),
    path('create_joblisting', views.create_joblisting, name='create_joblisting'),
    path('delete_joblisting/<int:id>', views.delete_joblisting, name='delete_joblisting'),
    path('jobs/', views.index, name='job_list'),

]
