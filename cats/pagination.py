# cats/pagination.py
from rest_framework.pagination import PageNumberPagination, BasePagination
from rest_framework.response import Response
class CatsPagination(PageNumberPagination):
    page_size = 1
class SomePagination(BasePagination):
    def get_paginated_response(self, data):
        return (Response({
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
            }))