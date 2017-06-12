from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Animal
from .serializers import AnimalSerializer


# Indent Cmd + Alt + L

class AnimalTask(APIView):
    def get(self, request, format=None):
        name = request.GET.get('name')
        if name:
            animal = Animal.objects.get(name=name)
        else:
            animals = Animal.objects.all()
            serializer = AnimalSerializer(animals, many=True)
            return Response(serializer.data)

        if animal:
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, format=None):
        name = request.GET.get('name')
        animal = Animal.objects.get(name=name)
        if animal:
            serializer = AnimalSerializer(animal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        name = request.GET.get('name')
        animal = Animal.objects.get(name=name)
        if animal:
            animal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
