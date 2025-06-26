from .models import Student
from  rest_framework import serializers

# Serializer Class
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'