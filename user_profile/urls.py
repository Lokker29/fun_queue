from django.urls import path

from user_profile import views

app_name = 'user_profile'

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create_group/', views.UniGroupCreateView.as_view(), name='create_group'),
]
