# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Employee(models.Model):
    """
    Empoloyee Model
    Defines the attributes of a employee
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    employee_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.first_name + ' is added.'

    def __str__(self):
        return "%s" % (self.first_name + " " + self.last_name)




class Device(models.Model):
    """
    Debvice Model
    Defines the attributes of a device
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device_id = models.IntegerField(primary_key=True)
    device_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.device_name + ' is added.'