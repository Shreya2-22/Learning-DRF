from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView, name="student-detail"),

    path('employees/', views.Employees.as_view(), name="employee-list"),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name="employee-detail"),
]
