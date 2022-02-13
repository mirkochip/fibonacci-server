from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.v1.fibonacci.serializers import FibonacciOutputSerializer
from src.api.v1.fibonacci.views_models import FibonacciViewsModels


class FibonacciView(APIView):

    @staticmethod
    def get(request):
        output_serializer = FibonacciOutputSerializer
        next_fibonacci_value = FibonacciViewsModels().get_next_fibonacci_value()
        return Response(
            status=status.HTTP_200_OK,
            data=output_serializer(next_fibonacci_value).data
        )

    @staticmethod
    def delete(request):
        FibonacciViewsModels().reset_fibonacci_series()
        return Response(status=status.HTTP_200_OK)
