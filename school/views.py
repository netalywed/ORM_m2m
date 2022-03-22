from django.views.generic import ListView
from django.shortcuts import render
from .models import Student, Teacher, TeachersOfStudent


def students_list(request):
    template = 'school/students_list.html'
    students_list = Student.objects.all()
    context = {'object_list': students_list}
    # teachers_list = Teacher.objects.all()
    # context = {'object_list': teachers_list}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)


