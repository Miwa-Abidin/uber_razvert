from django.shortcuts import render
from .models import Taxi, Order, StatusDriver, StatusType
from rest_framework import generics, viewsets
from .serializers import TaxiSerializer, OrderSerializer, StatusDriverSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsDriverOrReadOnly, IsOwnerOrReadOnly, IsClientOrReadOnly, IsAuthenticated, IsTrueOrReadOnly, IsFalseOrReadOnly

class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsDriverOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)



    # @action(methods=['POST'], detail=True)
    # def leave_status(self, request, pk=None):
    #     serializer = StatusDriverSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(
    #             taxi=self.get_object(),
    #             profile=request.user.profile
    #         )
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaxiRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer
    permission_classes = [IsTrueOrReadOnly, IsDriverOrReadOnly]


class OrderViewSet(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsClientOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class OrderRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsClientOrReadOnly, IsAuthenticatedOrReadOnly]



class StatusDriverViewSet(viewsets.ModelViewSet):
    queryset = StatusDriver.objects.all()
    serializer_class = StatusDriverSerializer
    permission_classes = [IsAuthenticated, IsClientOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)





