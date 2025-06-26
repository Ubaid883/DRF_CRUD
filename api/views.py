from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

# Create funcation based view here
@api_view(['GET','POST'])
def student_view(request):
    if request.method == 'GET':
        # get all student data
        student = Student.objects.all()
        # Convert complex data into json formate
        serializer = StudentSerializer(student, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
       serializer = StudentSerializer(data = request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response({'error':'Data Not Created'}, status=status.HTTP_400_BAD_REQUEST)

        
    
# Search student data by id
@api_view(['GET','PUT','DELETE'])
def student_details(request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({'error': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
        if request.method =='GET':
            serializer = StudentSerializer(student)
            return Response (serializer.data)
        elif request.method =='PUT':
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method =='DELETE':
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)