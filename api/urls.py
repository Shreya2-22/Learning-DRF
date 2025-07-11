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
    path('blogs/', views.BlogsView.as_view(), name="blog-list"),
    path('comments/', views.CommentsView.as_view(), name="comment-list"),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name="blog-detail"),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name="comment-detail"),
]
