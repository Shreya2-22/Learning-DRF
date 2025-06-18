from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
    students ={"name": "Alice", "age": 20}
    return JsonResponse(students)
