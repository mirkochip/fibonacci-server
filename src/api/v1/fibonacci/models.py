from django.db import models


class FibonacciSeries(models.Model):
    value = models.BigIntegerField()
