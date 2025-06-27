from django.urls import path
from .views import EmployeeView, EmployeeDetails

urlpatterns = [

    path('employee', EmployeeView.as_view(), name='Employee'),
    path('employee/<int:pk>', EmployeeDetails.as_view(), name='Employee'),

]
