from src.api.v1.fibonacci.models import FibonacciSeries
from src.common.config import BACK_STEPS


class FibonacciViewsModels:

    def get_next_fibonacci_value(self):
        fibonacci_series = FibonacciSeries.objects.all()
        fibonacci_entries = len(fibonacci_series)

        if fibonacci_entries < BACK_STEPS:
            self.set_fibonacci_series(fibonacci_entries)
            return FibonacciSeries.objects.latest('value')

        fibonacci_values = [fibonacci_item.value for fibonacci_item in fibonacci_series]
        next_fibonacci_value = fibonacci_values[-1] + fibonacci_values[-2]
        self.set_fibonacci_series(next_fibonacci_value)
        return FibonacciSeries.objects.latest('value')

    @staticmethod
    def set_fibonacci_series(value):
        FibonacciSeries(value=value).save()
