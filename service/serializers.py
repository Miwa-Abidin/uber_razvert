from .models import Taxi, StatusType, Order, StatusDriver
from rest_framework import serializers
from django.db import IntegrityError


from rest_framework.generics import get_object_or_404

class TaxiSerializer(serializers.ModelSerializer):
    statuses = serializers.ReadOnlyField(source='get_status_count')

    class Meta:
        model = Taxi
        fields = '__all__'
        read_only_fields = ['profile']


class StatusDriverSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(write_only=True)
    point = serializers.CharField(write_only=True, max_length=20)

    class Meta:
        model = StatusDriver
        fields = '__all__'
        read_only_fields = ['profile', 'point', 'type']


    def create(self, validated_data):
        status_type = get_object_or_404(StatusType, slug=validated_data['slug'])
        validated_data.pop('slug')
        validated_data['type'] = status_type
        try:
            instance = super().create(validated_data)
        except IntegrityError:
            status_driver = StatusDriver.objects.filter(**validated_data).first()
            if status_driver:
                status_driver.delete()
                raise serializers.ValidationError('У данного заказа есть статус, текуш стат удален')
            else:
                status_type = validated_data.pop('type')
                status_driver = StatusDriver.objects.get(**validated_data)
                status_driver.type = status_type
                status_driver.save()
                instance = status_driver

        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['adress', 'profile']