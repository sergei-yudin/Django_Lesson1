from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    date = DateFromToRangeFilter()
    status = filters.CharFilter(field_name="status")

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['date', 'status']
