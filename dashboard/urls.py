from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('signup/', views.signup_view)
]