from rest_framework import serializers

from cars.models import Car
from cars.serializers.car_feature import CarFeatureSerializer
from cars.serializers.car_image import CarImageSerializer


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True)
    features = CarFeatureSerializer(many=True)
    type_name = serializers.CharField(source='get_type_display')

    class Meta:
        model = Car
        fields = [
            'id',
            'make',
            'model_name',
            'description',
            'model_year',
            'price',
            'type',
            'type_name',
            'images',
            'title',
            'description',
            'features'
        ]


class CarCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'make',
            'model_name',
            'description',
            'model_year',
            'price',
            'type',
            'title',
            'description',
        ]
