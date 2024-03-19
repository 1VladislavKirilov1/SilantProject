from rest_framework import serializers
from .models import Car, Technic, Engine, Transmission, DrivingBridge, ControlledBridge
from my_silant.serializers import ServiceCompanySerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TechnicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technic
        fields = '__all__'


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'


class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = '__all__'


class DrivingBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivingBridge
        fields = '__all__'


class ControlledBridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlledBridge
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    technic = TechnicSerializer()
    engine = EngineSerializer()
    transmission = TransmissionSerializer()
    driving_bridge = DrivingBridgeSerializer()
    controlled_bridge = ControlledBridgeSerializer()
    service_company = ServiceCompanySerializer()
    client = UserSerializer()

    class Meta:
        model = Car
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['technic'] = TechnicSerializer(instance.technic).data
        representation['engine'] = EngineSerializer(instance.engine).data
        representation['transmission'] = TransmissionSerializer(instance.transmission).data
        representation['driving_bridge'] = DrivingBridgeSerializer(instance.driving_bridge).data
        representation['controlled_bridge'] = ControlledBridgeSerializer(instance.controlled_bridge).data
        representation['service_company'] = ServiceCompanySerializer(instance.service_company).data
        representation['client'] = UserSerializer(instance.client).data
        return representation
