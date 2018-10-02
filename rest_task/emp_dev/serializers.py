from rest_framework import serializers
from .models import Employee, Device

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('url', 'first_name', 'last_name', 'employee_id')


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('url', 'device_id', 'device_name', 'employee')    
