from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# For GET & POST methods
class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# Returning the single object as List
class PersonDetail(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    # returns a list
    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('name', None)
        return queryset.filter(name=name)

# GET Individual, PUT, DELETE
class PDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        name = self.request.query_params.get('name', None)
        return queryset.filter(name=name)

    # Returns a particular object from the list (based on parameters)
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj