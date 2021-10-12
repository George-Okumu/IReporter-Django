from django.conf.urls import url
from django.urls import path
from .views import RegistrationAPIView, VerifyEmail, LoginView

urlpatterns =[
    path('register', RegistrationAPIView.as_view(), name="register"),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email'),
    path('login', LoginView.as_view(), name='login'),

]