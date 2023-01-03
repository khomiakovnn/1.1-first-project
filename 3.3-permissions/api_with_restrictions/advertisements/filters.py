from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    status = filters.CharFilter()
    created_at = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ('status', 'created_at')
