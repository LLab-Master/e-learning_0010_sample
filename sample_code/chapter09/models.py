from django.db import models

# class Sample1(models.Model):
#     name = models.CharField(max_length=30)  # max_length は必須
#     age = models.IntegerField()
#     birthday = models.DateField()

#     def __str__(self):
#         return f'{self.name} {self.age} {self.birthday}'

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

 