from django.test import TestCase

from src.api.v1.fibonacci.models import FibonacciSeries


class TestFibonacciView(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create the first 5 entries
        entries = [0, 1, 1, 2, 3]
        for entry in entries:
            FibonacciSeries.objects.create(value=entry)

    def test_get(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['value'], 5)

    def test_delete(self):
        response = self.client.delete("/")
        self.assertEqual(response.status_code, 200)
