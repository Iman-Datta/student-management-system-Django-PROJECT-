from django.urls import path
from resultAPP import views


urlpatterns = [
    path('add-result/', views.teacher_result_view, name='_result'),
    path('results/view/', views.student_result_view, name='_student_result_view'),
    path('edit/<int:marksheet_id>/', views.edit_result_view, name='edit_result'),
]