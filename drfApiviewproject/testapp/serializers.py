from rest_framework import serializers

class Nameserializer(serializers.Serializer):
	name=serializers.CharField(max_length=50)