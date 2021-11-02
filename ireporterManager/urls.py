from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
      openapi.Info(
         title="IREPORTER API",
         default_version='v1',
         description="Ireporter Api that implements Authentication and Ireporter App Functionalities",
         contact=openapi.Contact(email="kevinleparwa@gmail.com"),
         license=openapi.License(name="No License"),
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
   )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('authenticationApp.urls')),
    path('api/', include('ireporterApp.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]