from django.contrib import admin
from django.urls import path
from to_do_list import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project/add/', views.ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('project/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/add_task/', views.TaskAddView.as_view(), name='task_add_to_project'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]