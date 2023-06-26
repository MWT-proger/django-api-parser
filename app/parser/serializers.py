from rest_framework import serializers


class TnvedSerializer(serializers.Serializer):
    number = serializers.CharField()
    name = serializers.CharField()

class DataTnvedSerializer(serializers.Serializer):
    data = TnvedSerializer(many=True)
