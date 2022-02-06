from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    object_list=Student.objects.all()
    teacher_list=Teacher.objects.all()

    context = {'object_list': object_list,
               'teacher_list': teacher_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)