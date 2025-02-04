from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'
