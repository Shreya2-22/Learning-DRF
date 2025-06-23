import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(lookup_expr='iexact', field_name='designation')
    emp_name = django_filters.CharFilter(lookup_expr='icontains', field_name='emp_name')
    id = django_filters.RangeFilter(field_name='id')

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id']