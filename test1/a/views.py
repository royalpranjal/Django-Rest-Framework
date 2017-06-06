from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def person_list(request, format=None):
    if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            person = Person.objects.filter(email=email)
        else:
            person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        email = request.GET.get('email')
        if email:
            person = Person.objects.get(email=email)
            serializer = PersonSerializer(person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        email = request.GET.get('email')
        person = Person.objects.filter(email=email)
        if person:
            person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

