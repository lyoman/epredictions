from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class PredictionLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class PredictionPageNumberPagination(PageNumberPagination):
    page_size = 10