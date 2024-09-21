from django.shortcuts import render

from rest_framework import generics
from .models import Animal
from .serializers import AnimalSerializer


class AnimalCreateView(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDeleteView(generics.DestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetailView(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
