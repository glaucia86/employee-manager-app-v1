from rest_framework import generics
from .serializers import EmployeeListSerializer
from .models import EmployeeList

from django.shortcuts import render


# Essa classe será responsável por criar o comportamento da nossa api:
# O 'ListCreateAPIVIEW' retorna os requests: [GET] & [POST]
class CreateView(generics.ListCreateAPIView):
    queryset = EmployeeList.objects.all()
    serializer_class = EmployeeListSerializer

    #Aqui irei salvar os dados via 'post' quando for criar um novo 'employee':
    def perform_create(self, serializer):
        serializer.save()

#Essa classe será responsável por manipular os métodos http: GET, PUT e DELETE:
# O 'RetrieveUpdateDestroyAPIView' é uma view genérica que provê os métodos: GET (by Id), PUT, PATCH & DELETE
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeList.objects.all()
    serializer_class = EmployeeListSerializer