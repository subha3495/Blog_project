from django.shortcuts import render
from django.views.generic import View
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from testapp.serializers import EmployeeSerializers
from testapp.models import Employee
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        id = pdata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serilizers=EmployeeSerializers(emp)
            json_data=JSONRenderer().render(serilizers.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serializer=EmployeeSerializers(qs,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer=EmployeeSerializers(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'resources created sucessfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data  = request.body
        stream     = io.BytesIO(json_data)
        pdata      = JSONParser().parse(stream)
        id         = pdata.get('id')
        emp        = Employee.objects.get(id=id)
        serializer = EmployeeSerializers(emp,data=pdata,partial=True)

        if serializer.is_valid():
            serializer.save()
            msg={'msg':'resources updated sucessfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json',status=400)

    def delete(self,request,*args,**kwargs):
        json_data  = request.body
        stream     = io.BytesIO(json_data)
        pdata      = JSONParser().parse(stream)
        id         = pdata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg={'msg':'resources deleted sucessfully'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')
       

  