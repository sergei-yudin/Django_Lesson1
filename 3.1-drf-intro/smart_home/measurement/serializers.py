from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor','temperature', 'created_at']
        extra_kwargs = {
            'sensor': {'write_only': True}
        }




class SensorSerializer(serializers.ModelSerializer):
        measurements = MeasurementSerializer(read_only=True, many=True)
        class Meta:
            model = Sensor
            fields = ['id', 'name', 'description', 'measurements']






# TODO: опишите необходимые сериализаторы
