from rest_framework import serializers

from cars.models import Car, CarFeature, CarImage


class CarFeatureCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    image_description = serializers.CharField(max_length=30, required=False)

    class Meta:
        model = CarFeature
        fields = [
            'image',
            'image_description',
            'title',
            'description',
        ]

    def validate(self, attrs):
        if not ('image' in attrs) and ('image_description' in attrs) or \
               ('image' in attrs) and not ('image_description' in attrs):
            error = 'Please send both image and image_description or none'
            raise serializers.ValidationError(error)

        return attrs

    def create(self, validated_data):
        """ Handle CarImage upload """
        image = validated_data.pop('image', None)
        image_description = validated_data.pop('image_description', None)

        car_image = None
        if image and image_description:
            car_image = CarImage.objects.create(
                file=image,
                image_description=image_description
            )

        return CarFeature.objects.create(**validated_data, image=car_image)


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = [
            'id',
            'file',
            'image_description',
        ]


class CarFeatureSerializer(serializers.ModelSerializer):
    image = CarImageSerializer()

    class Meta:
        model = CarFeature
        fields = [
            'id',
            'image',
            'title',
            'description',
        ]


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
