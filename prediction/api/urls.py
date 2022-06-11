from django.contrib import admin
from django.urls import path

from .views import (
    PredictionListAPIView,
    PredictionDeleteAPIView,
    PredictionDetailAPIView,
    PredictionUpdateAPIView,
    PredictionCreateAPIView,
    
    #######################################
    PredictionParameterListAPIView,
    PredictionParameterDeleteAPIView,
    PredictionParameterDetailAPIView,
    PredictionParameterUpdateAPIView,
    PredictionParameterCreateAPIView,
	)

urlpatterns = [
    path('prediction/', PredictionListAPIView.as_view(), name='list'),
    path('prediction/new/', PredictionCreateAPIView.as_view(), name='new'),
    path('prediction/<int:id>/detail/', PredictionDetailAPIView.as_view(), name='detail'),
    path('prediction/<int:id>/edit/', PredictionUpdateAPIView.as_view(), name='update'),
    path('prediction/<int:id>/delete/', PredictionDeleteAPIView.as_view(), name="delete"),
    
    path('prediction/parameter/', PredictionParameterListAPIView.as_view(), name='list_parameter'),
    path('prediction/parameter/new/', PredictionParameterCreateAPIView.as_view(), name='new_parameter'),
    path('prediction/parameter/<int:id>/detail/', PredictionParameterDetailAPIView.as_view(), name='detail_parameter'),
    path('prediction/parameter/<int:id>/edit/', PredictionParameterUpdateAPIView.as_view(), name='update_parameter'),
    path('prediction/parameter/<int:id>/delete/', PredictionParameterDeleteAPIView.as_view(), name="delete_parameter"),
]
