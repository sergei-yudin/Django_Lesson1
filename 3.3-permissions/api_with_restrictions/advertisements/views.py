from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOnReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOnReadOnly]


    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров


    # def get_permissions(self):
    #     # если нужно добавить спец права для отдельного действия, делаем здесь
    #     if self.action == "create":
    #         return [IsAuthenticated()]
    #     return super().get_permissions()
