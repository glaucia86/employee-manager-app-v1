from django.test import TestCase
from .models import EmployeeList

#Esta classe irá definir o conjunto de testes para o modelo da classe: 'Employee':
class ModelTestCase(TestCase):

    #Essa função aqui será responsável por testar o cliente e as variáveis
    def setUp(self):
        self.employeelist_name = "Glaucia Lemos"
        self.employeelist = EmployeeList(name=self.employeelist_name)

        self.employeelist_email = "glaucia.lemos@luizalabs.com"
        self.employeelist = EmployeeList(name=self.employeelist_email)

        self.employeelist_departament = "Information Technology"
        self.employeelist = EmployeeList(name=self.employeelist_departament)
        

    #Essa função irá testar o modelo da classe:
    def test_model_can_create_a_employeelist(self):
        old_count = EmployeeList.objects.count()
        self.employeelist.save()
        new_count = EmployeeList.objects.count()
        self.assertNotEqual(old_count, new_count)



