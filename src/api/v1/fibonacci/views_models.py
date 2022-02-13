import logging

from src.api.v1.fibonacci.models import FibonacciSeries
from src.common.config import BACK_STEPS

logger = logging.getLogger('__name__')


class FibonacciViewsModels:

    def get_next_fibonacci_value(self):
        fibonacci_values = [fibonacci_item.value for fibonacci_item in FibonacciSeries.objects.all()]
        logger.debug(f'Partial Fibonacci sequence: {fibonacci_values}')
        fibonacci_n_entries = len(fibonacci_values)

        if fibonacci_n_entries < BACK_STEPS:
            self.set_fibonacci_series(fibonacci_n_entries)
            return FibonacciSeries.objects.latest('value')

        next_fibonacci_value = fibonacci_values[-1] + fibonacci_values[-2]
        self.set_fibonacci_series(next_fibonacci_value)
        return FibonacciSeries.objects.latest('value')

    @staticmethod
    def set_fibonacci_series(value):
        logger.info(f'Next Fibonacci sub-sequent item: {value}.')
        FibonacciSeries(value=value).save()

    @staticmethod
    def reset_fibonacci_series():
        FibonacciSeries.objects.all().delete()
        logger.info('Fibonacci sequence cleared.')
