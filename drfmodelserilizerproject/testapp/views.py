from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create y0our views here.

# class EmployeeAPIView(APIView):
# 	def get(self,request,format=None):
# 		qs=Employee.objects.all()
# 		serializer=EmployeeSerializer(qs,many=True)
# 		return Response(serializer.data)

# class EmployeeLISTAPIView(ListAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer

# 	def get_queryset(self):
# 		qs   = Employee.objects.all()
# 		name = self.request.GET.get('ename')
# 		if name is not None:
# 			qs = qs.filter(ename__icontains=name)
# 		return qs

# class EmployeeCreateAPIView(CreateAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer

# class EmployeeRetrieveAPIView(RetrieveAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer

# class EmployeeUpdateAPIView(UpdateAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer
# 	lookup_field = 'id'

# class EmployeeDestroyAPIView(DestroyAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer
# 	lookup_field = 'id'

# class EmployeeListCreateAPIView(ListCreateAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer

# class EmployeeRetriveUpdateAPIView(RetrieveUpdateAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer
# 	lookup_field = 'id'

# class EmployeeRetriveDestroyAPIView(RetrieveDestroyAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer
# 	lookup_field = 'id'

# class EmployeeRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset = Employee.objects.all()
# 	serializer_class = EmployeeSerializer
# 	lookup_field = 'id'


from rest_framework import mixins

class EmployeeListCreateModelmixins(mixins.CreateModelMixin,ListAPIView):

	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

class EmployeeRetriveUpdateDestroyModelmixins(mixins.DestroyModelMixin,mixins.UpdateModelMixin,RetrieveAPIView):

	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def patch(self,request,*args,**kwargs):
		return self.partial_update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)