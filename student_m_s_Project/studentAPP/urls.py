from django.urls import path
from studentAPP import views

urlpatterns = [
    path('payment/', views.payment, name='_payment')
]