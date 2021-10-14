from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('authenticationApp.urls')),
    path('api/', include('ireporterApp.urls')),
]