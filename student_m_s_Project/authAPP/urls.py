from django.urls import path
from authAPP import views

urlpatterns = [
    path('login/', views.login, name='_login'),
    path('create_account/', views.create_account, name='_create_account'),
    path('logout/', views.logout, name='_logout'),
]