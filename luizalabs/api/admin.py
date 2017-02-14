from django.contrib import admin
from .models import EmployeeList

class EmployeeAdmin(admin.ModelAdmin):
    model = EmployeeList
    list_display = ('id', 'name', 'email', 'department')
    list_filter = ('name', 'email', 'department')
    search_fields = ('name', 'email', 'department')

admin.site.register(EmployeeList, EmployeeAdmin)
