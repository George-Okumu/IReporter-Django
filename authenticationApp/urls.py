from django.conf.urls import url
from django.urls import path
from .views import RegistrationAPIView, VerifyEmail, LoginView, AdminLoginView, AdminRegistrationAPIView

urlpatterns =[
    path('register', RegistrationAPIView.as_view(), name="register"),
    path('admin/register', AdminRegistrationAPIView.as_view(), name="admin-register"),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email'),
    path('admin/login', AdminLoginView.as_view(), name='admin-login'),
    path('login', LoginView.as_view(), name='login'),

]