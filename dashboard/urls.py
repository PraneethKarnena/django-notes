from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('signup/', views.signup_view, name='signup_page'),
    path('signin/', views.signin_view, name='signin_page'),
    path('signout/', LogoutView.as_view(), name='signout_page'),
    path('dashboard/', views.dashboard_view, name='dashboard_page'),
    path('api/my-notes/', views.my_notes_api, name='my_notes_api'),
]