from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('admin/', admin.site.urls),
    path('sign-up', views.signup, name='Sign-up'),
    path('sign-in', views.signin, name='signin'),
]