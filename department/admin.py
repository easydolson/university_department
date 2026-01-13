from django.contrib import admin
from .models import *

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'room', 'phone', 'email']
    search_fields = ['name', 'room']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'position', 'rate', 'classroom']
    list_filter = ['position', 'rate', 'classroom']
    search_fields = ['last_name', 'first_name', 'middle_name']
    list_editable = ['rate', 'classroom']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'semester', 'get_employees']
    list_filter = ['semester']
    search_fields = ['name', 'code']

    def get_employees(self, obj):
        return ", ".join([str(e) for e in obj.employees.all()])

    get_employees.short_description = 'Преподаватели'

@admin.register(Teaching)
class TeachingAdmin(admin.ModelAdmin):
    list_display = ['employee', 'subject', 'hours_per_week', 'is_responsible']
    list_filter = ['is_responsible', 'subject__semester']

@admin.register(AdditionalWork)
class AdditionalWorkAdmin(admin.ModelAdmin):
    list_display = ['employee', 'work_type', 'hours_per_month', 'is_active']
    list_filter = ['work_type', 'is_active']
    search_fields = ['employee__last_name', 'description']

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'capacity', 'description']
    search_fields = ['room_number']