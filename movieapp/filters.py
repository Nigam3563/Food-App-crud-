from .models import  Movies
import django_filters


class MoviesFilter(django_filters.FilterSet):
    class Meta:
        model = Movies
        fields = ['name', 'rating']
