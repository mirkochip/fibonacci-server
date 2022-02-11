from django.urls import path

from src.api.v1.fibonacci.views import FibonacciView

urlpatterns = [
    path('', FibonacciView.as_view(http_method_names=['get', 'delete', ])),
]
