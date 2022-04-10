from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('sign-up', views.signup, name='Sign-up'),
]