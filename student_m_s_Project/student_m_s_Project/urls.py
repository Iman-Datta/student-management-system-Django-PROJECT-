from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('studentAPP.urls')),
    path('auth/', include('authAPP.urls'))
]