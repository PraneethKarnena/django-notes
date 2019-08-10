from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('signup/', views.signup_view, name='signup_page'),
    path('signin/', views.signin_view, name='signin_page'),
]