from django.contrib import admin

from cars.models import Car, CarImage, CarFeature


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'make',
        'model_name',
        'model_year',
        'price',
        'type',
    )


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_description', 'file')


@admin.register(CarFeature)
class CarFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'description')
