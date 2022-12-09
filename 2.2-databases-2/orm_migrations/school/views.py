from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'
    object_list = Student.objects.all().prefetch_related('teachers').order_by(ordering)
    context = {
        'object_list': object_list,
    }
    return render(request, template, context)
