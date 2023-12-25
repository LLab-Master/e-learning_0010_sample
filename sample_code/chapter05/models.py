from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.id}:{self.name}'

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.product}'
