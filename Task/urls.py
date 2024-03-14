from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('tasks/', views.TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='task-list'),
    path('tasks/<int:pk>/', views.TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='task-detail'),
    path('dashboard/task/', views.DashboardTaskCompletionStatViewSet.as_view({'get': 'list'}), name='task-completion-stats'),
    path('dashboard/task-with-category/', views.DashboardTaskByCategoryViewSet.as_view({'get': 'list'}), name='task-by-category'),
]
