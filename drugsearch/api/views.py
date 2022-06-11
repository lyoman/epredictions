from rest_framework.generics import ListAPIView

from drugsearch.models import DrugSearch
# from .serializers import DrugSearchSerializer

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

from .pagination import DrugSearchLimitOffSetPagination , DrugSearchPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    DrugSearchListSerializer,
    DrugSearchDetailSerializer, 
    DrugSearchCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

#Creating an DrugSearch
class DrugSearchCreateAPIView(CreateAPIView):
    queryset = DrugSearch.objects.all()
    serializer_class = DrugSearchCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class DrugSearchUpdateAPIView(RetrieveUpdateAPIView):
    queryset = DrugSearch.objects.all()
    serializer_class = DrugSearchCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class DrugSearchDeleteAPIView(DestroyAPIView):
    queryset = DrugSearch.objects.all()
    serializer_class = DrugSearchDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class DrugSearchDetailAPIView(RetrieveAPIView):
    queryset = DrugSearch.objects.all()
    serializer_class = DrugSearchDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class DrugSearchListAPIView(ListAPIView):
    serializer_class = DrugSearchListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    # pagination_class = DrugSearchPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = DrugSearch.objects.filter()
        id = self.request.query_params.get('name', None)
        if id is not None:
            queryset = queryset.filter(name=id)
            print("hey you", queryset)
        return queryset


class DrugSearchUserListAPIView(ListAPIView):
    serializer_class = DrugSearchListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    # pagination_class = DrugSearchPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = DrugSearch.objects.filter()
        id = self.request.query_params.get('location', None)
        if id is not None:
            queryset = queryset.filter(location=id)
            print("hey you", queryset)
        return queryset