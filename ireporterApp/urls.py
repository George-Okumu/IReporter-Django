from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RedFlagDetail, RedFlagList

urlpatterns = [
    path('redflag', RedFlagList.as_view(), name='red-flag-list'),
    path('redflag/<int:pk>/', RedFlagDetail.as_view(), name='red-flag-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)