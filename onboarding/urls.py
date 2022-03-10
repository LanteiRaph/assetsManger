from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register-user/', views.RegisterUser.as_view(), name='register-user'),
]