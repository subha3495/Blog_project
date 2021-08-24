from rest_framework import serializers
from .models import Employee


def multipuls_of_1000(value):
    if value % 1000 !=0:
        raise serializers.ValidationError('Employee salary should be multipuls of 1000')

class EmployeeSerializers(serializers.ModelSerializer):
    esal   = serializers.FloatField(validators=[multipuls_of_1000])
    class Meta:
        model  = Employee
        fields = '__all__'




# class EmployeeSerializers(serializers.Serializer):
#     eid  = serializers.IntegerField()
#     ename= serializers.CharField(max_length=50)
#     esal = serializers.IntegerField(validators=[multipuls_of_1000])
#     eadd = serializers.CharField(max_length=50)

#     def validate_esal(self,value):
#         if value <5000:
#             raise serializers.ValidationError('Employee salary should be minum 5000')
#         return value

#     def validate(self,data):
#         ename = data.get('ename')
#         esal  = data.get('esal')
#         if ename.lower()== 'sunny':
#             if esal<50000:
#                 raise serializers.ValidationError('Sunny salary should be minum 50000')
#         return data


#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data)


#     def update(self,instance,validated_data):
#         instance.eid=validated_data.get('eid',instance.eid)
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eadd=validated_data.get('eadd',instance.eadd)
#         instance.save()

#         return instance