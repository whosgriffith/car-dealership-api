from rest_framework import serializers

from cars.models import CarImage


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = [
            'id',
            'file',
            'image_description',
        ]
