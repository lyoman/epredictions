from rest_framework.generics import ListAPIView

from prediction.models import Prediction, PredictionParameter
# from .serializers import PredictionSerializer

from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)

from .pagination import PredictionLimitOffSetPagination , PredictionPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    PredictionListSerializer,
    PredictionDetailSerializer, 
    PredictionCreateUpdateSerializer,
    
    PredictionParameterListSerializer,
    PredictionParameterDetailSerializer, 
    PredictionParameterCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


#Creating an Ambulance
class PredictionCreateAPIView(CreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    
    
class PredictionUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class PredictionDeleteAPIView(DestroyAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class PredictionDetailAPIView(RetrieveAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class PredictionListAPIView(ListAPIView):
    serializer_class = PredictionListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['disease']
    pagination_class = PredictionPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Prediction.objects.filter(active=True)
        id = self.request.query_params.get('disease', None)
        if id is not None:
            queryset = queryset.filter(disease=id)
            print("hey you", queryset)
        return queryset
    
    

##################Prediction Parameters#########################

#Creating a Parameter
class PredictionParameterCreateAPIView(CreateAPIView):
    queryset = PredictionParameter.objects.all()
    serializer_class = PredictionParameterCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    
    
class PredictionParameterUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PredictionParameter.objects.all()
    serializer_class = PredictionParameterCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class PredictionParameterDeleteAPIView(DestroyAPIView):
    queryset = PredictionParameter.objects.all()
    serializer_class = PredictionParameterDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class PredictionParameterDetailAPIView(RetrieveAPIView):
    queryset = PredictionParameter.objects.all()
    serializer_class = PredictionParameterDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class PredictionParameterListAPIView(ListAPIView):
    serializer_class = PredictionParameterListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['disease']
    # pagination_class = PredictionPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Prediction.objects.filter(active=True)
        id = self.request.query_params.get('disease', None)
        if id is not None:
            queryset = queryset.filter(disease=id)
            print("hey you", queryset)
        return queryset