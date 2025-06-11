from adoption.models import Pet
from adoption.serializers import PetSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend


class PetsList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'breed']
    filterset_fields = ['species', 'age']


class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer