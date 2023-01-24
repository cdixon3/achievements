from django.urls import path
from . import views

urlpatterns = [
    path('task_executions/', views.task_execution_list)
]