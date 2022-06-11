from django.contrib import admin
from django.urls import path

from .views import (
    PredictionListAPIView,
    PredictionDeleteAPIView,
    PredictionDetailAPIView,
    PredictionUpdateAPIView,
    PredictionCreateAPIView,
	)

urlpatterns = [
    path('prediction/', PredictionListAPIView.as_view(), name='list'),
    path('prediction/new/', PredictionCreateAPIView.as_view(), name='new'),
    path('prediction/<int:id>/detail/', PredictionDetailAPIView.as_view(), name='detail'),
    path('prediction/<int:id>/edit/', PredictionUpdateAPIView.as_view(), name='update'),
    path('prediction/<int:id>/delete/', PredictionDeleteAPIView.as_view(), name="delete"),
]
