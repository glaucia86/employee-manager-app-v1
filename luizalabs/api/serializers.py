from rest_framework import serializers
from .models import EmployeeList

#Aqui estou mapeando a instância da classe modelo para o formato JSON:
class EmployeeListSerializer(serializers.ModelSerializer):

    #O 'Meta' irá mapear os campos serializados com os campos da classe modelo:
    class Meta:
        model = EmployeeList
        fields = ('id', 'name', 'email', 'department')
