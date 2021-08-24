from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import Nameserializer
# Create your views here.

class TestAPIView(APIView):

	def get(self,*args,**kwargs):
		colors=['red','white','black']
		return Response({'msg':'Happy Makar Sankranti','colors':colors})

	def post(self,request,*args,**kwargs):
		serializer = Nameserializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			msg  = 'Hello {} Happy Holli'.format(name)
			return Response({'msg':msg})
		else:
			return Response(serializer.errors,status=400)

	def put(self,*args,**kwargs):
		return Response({'msg':'This the APIView put method'})

	def patch(self,*args,**kwargs):
		return Response({'msg':'This is the APIView patch method'})

	def delete(self,*args,**kwargs):
		return Response({'msg':'This is the APIView delete method'})

from rest_framework.viewsets import ViewSet

class TestViewSet(ViewSet):

	def list(self,request):
		colors=['red','white','black']
		return Response({'msg':'Happy New year','colors':colors})

	def create(self,request):
		serializer = Nameserializer(data = request.data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			msg  = 'Hello {} Happy Holli'.format(name)
			return Response({'msg':msg})
		else:
			return Response(serializer.errors,status=400)
