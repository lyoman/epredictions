from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class DrugSearchLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class DrugSearchPageNumberPagination(PageNumberPagination):
    page_size = 10