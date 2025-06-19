from django.urls import path
from studentAPP import views

urlpatterns = [
    # path('home/', views.home, name='_home'),
    path('result/', views.result, name='_result'),
    path('payment/', views.payment, name='_payment'),
    path('registration/', views.registration, name='_registration'),
]