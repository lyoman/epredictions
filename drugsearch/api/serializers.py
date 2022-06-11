from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from drugsearch.models import DrugSearch
# from .serializers import PostSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


#####Process flow Charts
class DrugSearchCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = DrugSearch
        fields = [
            'id',
            'name',
            "location", 
            "latitude", 
            "longitude"
        ]


soldstock_detail_url = HyperlinkedIdentityField(
        view_name='drugsearch-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class DrugSearchDetailSerializer(ModelSerializer):
    url = soldstock_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = DrugSearch
        fields = [
            'url',
            'id',
            'name',
            "location", 
            "latitude", 
            "longitude",
            'updated',
            'timestamp'
        ]

class DrugSearchListSerializer(ModelSerializer):
    url = soldstock_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='drugsearch-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = DrugSearch
        fields = [
            'url',
            'id',
            'delete_url',
            'name',
            "location", 
            "latitude", 
            "longitude",
            'updated',
            'timestamp'
        ]