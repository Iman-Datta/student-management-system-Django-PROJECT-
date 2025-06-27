from django.urls import path
from homeAPP import views

urlpatterns = [
    path('', views.home, name='_home'),
    path('after_login/', views.after_login, name='_after_login'),
]