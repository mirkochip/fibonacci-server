from django.test import TestCase

from src.api.v1.fibonacci.models import FibonacciSeries
from src.api.v1.fibonacci.views_models import FibonacciViewsModels


class TestFibonacciViewsModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create the first 7 entries
        values = [0, 1, 1, 2, 3, 5, 8]
        for value in values:
            FibonacciSeries.objects.create(value=value)

    def test_get_next_fibonacci_value_init(self):
        FibonacciSeries.objects.all().delete()
        self.assertEqual(len(FibonacciSeries.objects.all()), 0)
        next_value = FibonacciViewsModels().get_next_fibonacci_value().value
        self.assertEqual(next_value, 0)
        next_value = FibonacciViewsModels().get_next_fibonacci_value().value
        self.assertEqual(next_value, 1)

    def test_get_next_fibonacci_value_steps_back(self):
        next_value = FibonacciViewsModels().get_next_fibonacci_value().value
        self.assertEqual(next_value, 13)

    def test_set_fibonacci_series(self):
        FibonacciViewsModels().set_fibonacci_series(13)
        self.assertEqual(len(FibonacciSeries.objects.all()), 8)
