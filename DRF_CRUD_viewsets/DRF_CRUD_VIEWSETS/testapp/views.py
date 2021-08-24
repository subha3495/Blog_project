from django.shortcuts import render
from .models import Employee
from .serializers import Employeeserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions,IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from testapp.permissions import IsReadeonly
from testapp.authentications import CustomAuthentication
from testapp.pagenations import Mypagepagination,Mypage_limitoffset,Mypage_cusore
class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    # authentication_classes = [TokenAuthentication,]
    authentication_classes = [CustomAuthentication,]
    permission_classes = [IsReadeonly,]
    pagination_class = Mypagepagination
    search_fields = ('ename','eno')
    ordering_fields = ('eno','ename')

    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs = qs.filter(ename__icontains=name)
    #     return qs