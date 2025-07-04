from django.urls import path
from resultAPP import views


urlpatterns = [
    path('add-result/', views.add_result, name='_add_result'),
    # path('view-result/', views3.view_result, name='_view_result'),
    # path('update-result/', views3.update_result, name='_update_result'),
]