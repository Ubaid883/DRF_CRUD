from django.urls import path
from api import views

urlpatterns = [
    path('student',views.student_view, name='student'),
    path('student/<int:pk>',views.student_details, name='student-details'),
]
