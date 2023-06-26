from rest_framework import serializers

class ErrorsSerializer(serializers.Serializer):
    errors = serializers.CharField()


class TnvedSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()


class DataTnvedSerializer(serializers.Serializer):
    data = TnvedSerializer(many=True)


class Okpd2Serializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()


class DataOkpd2Serializer(serializers.Serializer):
    data = Okpd2Serializer()
