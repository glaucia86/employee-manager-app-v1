from django.contrib import admin
from .models import EmployeeList

class EmployeeAdmin(admin.ModelAdmin):
    model = EmployeeList
    list_display = ('id', 'name', 'email', 'departament')
    list_filter = ('name', 'email', 'departament')
    search_fields = ('name', 'email', 'departament')

admin.site.register(EmployeeList, EmployeeAdmin)
