from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny, IsAdminUser

from cars.models import Car, CarFeature, CarImage
from cars.serializers.car import CarCreateUpdateSerializer, CarSerializer
from cars.serializers.car_feature import (
    CarFeatureCreateSerializer,
    CarFeatureSerializer,
    CarFeatureUpdateSerializer
)
from cars.serializers.car_image import CarImageSerializer


class CarsViewSet(viewsets.ModelViewSet):
    """ ModelViewSet implements CRUD functionality """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'model_year']

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method in ["POST", "PATCH", "PUT", "DELETE"]:
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return CarSerializer
        elif self.request.method == "POST":
            return CarCreateUpdateSerializer
        elif self.action == "update":
            return CarCreateUpdateSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        type = self.request.query_params.get('type')
        if type:
            queryset = queryset.filter(type=type)
        return queryset


class FeaturesViewSet(viewsets.ModelViewSet):
    """ ModelViewSet implements CRUD functionality """
    queryset = CarFeature.objects.all()
    serializer_class = CarFeatureSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return CarFeatureSerializer
        elif self.request.method == "POST":
            return CarFeatureCreateSerializer
        elif self.action == "update":
            return CarFeatureUpdateSerializer


class CarImagesViewSet(viewsets.ModelViewSet):
    """ ModelViewSet implements CRUD functionality """
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method in ["POST", "DELETE", "PUT", "PATCH"]:
            return [IsAdminUser()]
        return [permission() for permission in self.permission_classes]
