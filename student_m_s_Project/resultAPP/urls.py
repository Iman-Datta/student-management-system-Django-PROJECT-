from django.urls import path
from resultAPP import views

urlpatterns = [
    path('add-result/', views.add_result, name='_add_result'),
    path('view-result/', views.view_result, name='_view_result'),
    path('update-result/', views.update_result, name='_update_result'),
]