from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homeAPP.urls')),
    path('auth/', include('authAPP.urls')),
    path('result/', include('resultAPP.urls')),
]