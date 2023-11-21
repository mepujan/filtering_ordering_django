from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializers
from .pagination import BookPagination
from .filters import PublicationFIlterRange
from rest_framework.filters import OrderingFilter


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title', 'author']
    filterset_class = PublicationFIlterRange
    ordering_fields = ['title', 'author', 'publication']
