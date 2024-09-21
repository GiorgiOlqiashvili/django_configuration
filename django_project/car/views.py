from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDeleteView(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
