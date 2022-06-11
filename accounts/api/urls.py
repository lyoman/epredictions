from django.urls import path
from django.contrib import admin
# from rest_framework_jwt.views import obtain_jwt_token# , CustomAuthToken
from rest_framework_jwt.views import obtain_jwt_token

from .views import (
    UserLoginAPIView,
    UserCreateAPIView,
    UserDetailAPIView,
    UserlistAPIView,
    UserUpdateAPIView
    )

urlpatterns = [
    path('', UserDetailAPIView.as_view(), name='users'),
    path('user_detail/<int:id>/', UserlistAPIView.as_view(), name='detail'),
    path('user/<int:id>/edit/', UserUpdateAPIView.as_view(), name='edit'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('api/auth/token/', obtain_jwt_token, name='token'),
]