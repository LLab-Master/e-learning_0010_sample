from django.db import models

class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f'{self.id}:{self.name}'

