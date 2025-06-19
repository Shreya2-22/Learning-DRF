from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 21},
    ]
    return HttpResponse(students)
    