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
