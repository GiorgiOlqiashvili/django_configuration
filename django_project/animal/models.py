from django.db import models


class Animal(models.Model):
    species = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.species}, {self.age})'

