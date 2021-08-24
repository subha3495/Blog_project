from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eadd']

admin.site.register(Employee,EmployeeAdmin)