from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

# Create funcation based view here
@api_view(['GET'])
def student_view(request):
    if request.method == 'GET':
        # get all student data
        student = Student.objects.all()
        # Convert complex data into json formate
        serializer = StudentSerializer(student, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    