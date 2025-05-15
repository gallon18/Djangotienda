from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login_view, name='Login'),
    path('logout/', views.Login_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
