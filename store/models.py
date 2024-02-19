from django.db import models


class Store(models.Model):






    price = models.FloatField()
    discount = models.IntegerField(default=0)
    price_with_discount = models.FloatField(default=0)
    brand = models.CharField(max_length=100)



    def calculate_discount(self):
        return (self.price / 100) * self.discount









