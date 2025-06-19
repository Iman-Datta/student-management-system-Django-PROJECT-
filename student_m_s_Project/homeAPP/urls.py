from django.urls import path
from homeAPP import views

urlpatterns = [
    path('', views.home, name='_home'),
]