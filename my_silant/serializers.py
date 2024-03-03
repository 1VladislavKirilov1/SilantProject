from rest_framework import serializers
from .models import *


class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = '__all__'


class TypeMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMaintenance
        fields = '__all__'


class FailureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Failure
        fields = '__all__'


class RecoveryMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'


class MaintenanceSerializer(serializers.ModelSerializer):
    type = TypeMaintenanceSerializer()
    service_company = ServiceCompanySerializer()

    class Meta:
        model = Maintenance
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    node_failure = FailureSerializer()
    method_recovery = RecoveryMethodSerializer()
    service_company = ServiceCompanySerializer()

    class Meta:
        model = Complaint
        fields = '__all__'
