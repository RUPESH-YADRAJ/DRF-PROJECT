from django.shortcuts import render
from django.http import HttpResponse


def students(request):
  student = [
    {'id': 1, 'Name': 'Ram', 'age':25}
  ]
  return HttpResponse(student)
