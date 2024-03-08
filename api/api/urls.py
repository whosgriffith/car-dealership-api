from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from cars.views import CarsViewSet, FeaturesViewSet, CarImagesViewSet
from authentication.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'cars/images', CarImagesViewSet)
router.register(r'cars/features', FeaturesViewSet)
router.register(r'cars', CarsViewSet)
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('documentation/', SpectacularSwaggerView.as_view(
        url_name='schema'),
        name='swagger-ui'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
