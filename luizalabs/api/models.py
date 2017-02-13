from django.db import models

#Definindo a classe: EmployeeList:
class EmployeeList(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    departament = models.CharField(max_length=50)


    #Aqui estou criando uma função para que retorne nome do empregado no admin:
    def __str__(self):
        return self.name
    