from django.contrib import admin
from django.urls import path

from .views import (
    DrugSearchListAPIView,
    DrugSearchDeleteAPIView,
    DrugSearchDetailAPIView,
    DrugSearchUpdateAPIView,
    DrugSearchCreateAPIView,
	)

urlpatterns = [
    ##### process flow
    path('results/', DrugSearchListAPIView.as_view(), name='list'),
    path('results/new/', DrugSearchCreateAPIView.as_view(), name='new'),
    path('results/<int:id>/detail/', DrugSearchDetailAPIView.as_view(), name='detail'),
    path('results/<int:id>/edit/', DrugSearchUpdateAPIView.as_view(), name='edit'),
    path('results/<int:id>/delete/', DrugSearchDeleteAPIView.as_view(), name="delete"),
]
