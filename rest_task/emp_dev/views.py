# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from models import Employee, Device
from serializers import EmployeeSerializer, DeviceSerializer

# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('employee_id')
    serializer_class = EmployeeSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('device_id')
    serializer_class = DeviceSerializer