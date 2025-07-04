from django.urls import path
from resultAPP import views


urlpatterns = [
    path('add-result/', views.result, name='_result'),
    path('results/view/', views.student_result_view, name='_student_result_view'),
]