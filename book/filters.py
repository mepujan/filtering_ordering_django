import django_filters
from .models import Book


class PublicationFIlterRange(django_filters.FilterSet):
    publication = django_filters.DateFromToRangeFilter()
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication']
