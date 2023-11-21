from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializers
from .pagination import BookPagination
from .filters import PublicationFIlterRange


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = BookPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']
    filterset_class = PublicationFIlterRange
