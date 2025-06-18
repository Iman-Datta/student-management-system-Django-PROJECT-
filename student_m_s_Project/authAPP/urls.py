from django.urls import path
from studentAPP import views

urlpatterns = [
    path('home', views.home, name='home'),
]