from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.QueueListView.as_view(), name='queue_list'),
    path('create_queue/', views.QueueCreateView.as_view(), name='create_queue'),
]
