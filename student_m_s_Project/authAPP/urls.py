from django.urls import path
from authAPP import views

urlpatterns = [
    path('login/', views.login_view, name='_login'),
    path('forgot_password/', views.forgot_password, name='_forgot_password'),
    path('create_account/', views.create_account, name='_create_account'),
    path('logout/', views.logout_view, name='_logout'),
]