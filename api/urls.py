from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView, name="student-detail"),

    # path('employees/', views.Employees.as_view(), name="employee-list"),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name="employee-detail"),

    path('', include(router.urls)),
]
