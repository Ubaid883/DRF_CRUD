from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    department = models.CharField(max_length=55)
    reg_number = models.IntegerField()
    address = models.CharField(max_length=255)
    major_subject = models.CharField(max_length=55, choices=[
        ('Computer', 'Computer'),
        ("Physics",'Physics'),
        ("Math",'Math'),
        ("Bio",'Bio'),
    ])