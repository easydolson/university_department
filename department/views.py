from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'department/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        position = self.request.GET.get('position')
        if position:
            queryset = queryset.filter(position=position)
        return queryset.order_by('last_name')


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'department/employee_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = self.object.teaching_set.all()
        context['additional_work'] = self.object.additionalwork_set.filter(is_active=True)
        return context


class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'department/subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        queryset = super().get_queryset()
        semester = self.request.GET.get('semester')
        if semester:
            queryset = queryset.filter(semester=semester)
        return queryset.order_by('semester', 'name')


@login_required
def dashboard(request):
    """Главная страница системы"""
    total_employees = Employee.objects.count()
    full_rate = Employee.objects.filter(rate=1.0).count()
    part_time = Employee.objects.exclude(rate=1.0).count()
    total_subjects = Subject.objects.count()
    active_work = AdditionalWork.objects.filter(is_active=True).count()

    context = {
        'total_employees': total_employees,
        'full_rate': full_rate,
        'part_time': part_time,
        'total_subjects': total_subjects,
        'active_work': active_work,
    }
    return render(request, 'department/dashboard.html', context)