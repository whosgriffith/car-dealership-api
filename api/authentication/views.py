from django.contrib.auth.models import User
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from authentication.serializers import (
    UserModelSerializer,
    UserSignUpSerializer,
    UserLoginSerializer
)


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        print(self.request.method)
        if self.request.method == "DELETE":
            return [IsAdminUser()]
        if self.action in ["signup", "login"]:
            return [AllowAny()]
        elif self.action == "retrieve":
            return [IsAuthenticated()]
        return [permission() for permission in self.permission_classes]

    @action(detail=False, methods=['POST'])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data=data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        return Response(data=response.data, status=status.HTTP_200_OK)
