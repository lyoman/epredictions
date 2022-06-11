from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from prediction.models import Prediction
# from .serializers import PostSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class PredictionCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Prediction
        fields = [
        'id',
        "user", 
        "patient_name", 
        "patient_id", 
        "disease", 
        "algorithm",
        "symptom_1", 
        "symptom_2", 
        "symptom_3", 
        "symptom_4",
        "symptom_4",
        "symptom_5",
        ]


prediction_detail_url = HyperlinkedIdentityField(
        view_name='prediction-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class PredictionDetailSerializer(ModelSerializer):
    url = prediction_detail_url
    class Meta:
        model = Prediction
        fields = [
            'url',
            'id',
            "user", 
            "patient_name", 
            "patient_id", 
            "disease", 
            "algorithm",
            "symptom_1", 
            "symptom_2", 
            "symptom_3", 
            "symptom_4",
            "symptom_4",
            "symptom_5",
            'updated',
            'timestamp'
        ]

class PredictionListSerializer(ModelSerializer):
    url = prediction_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='prediction-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = Prediction
        fields = [
            'url',
            'id',
            'delete_url',
            "user", 
            "patient_name", 
            "patient_id", 
            "disease", 
            "algorithm",
            "symptom_1", 
            "symptom_2", 
            "symptom_3", 
            "symptom_4",
            "symptom_4",
            "symptom_5",
            'updated',
            'timestamp'
        ]
