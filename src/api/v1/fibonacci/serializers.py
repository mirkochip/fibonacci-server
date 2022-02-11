from rest_framework.serializers import IntegerField, Serializer


class FibonacciOutputSerializer(Serializer):
    value = IntegerField()
