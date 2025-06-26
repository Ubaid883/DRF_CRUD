from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# Create funcation based view here
def student_view(request):
    # get all student data
    student = Student.objects.all()
    # Convert complex data into json formate
    serializer = StudentSerializer(student, many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    