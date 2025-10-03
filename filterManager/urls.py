from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filters/', include('filters.urls')),  # Inclure nos routes
]
