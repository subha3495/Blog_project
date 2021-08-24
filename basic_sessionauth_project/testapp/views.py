from django.shortcuts import render
from .models import Employee
from .serializers import Employeeserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    authentication_classes = [SessionAuthentication,]
    permission_classes = [IsAuthenticated,]


