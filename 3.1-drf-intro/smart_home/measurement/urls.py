from django.urls import path

from measurement.views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementCreateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementCreateAPIView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
