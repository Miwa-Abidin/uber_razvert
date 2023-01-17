from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework import status

from rest_framework import mixins

from . serializers import ProfileRegisterSerializer
from .models import Profile, User

class ProfileRegisterApiView(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileRegisterSerializer

    def create_profile(self, request, is_driver):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save(is_driver=is_driver)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["POST"], detail=False)
    def driver(self, request, pk=None):
        return self.create_profile(request, True)

    @action(methods=["POST"], detail=False)
    def client(self, request, pk=None):
        return self.create_profile(request, False)


