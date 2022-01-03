from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.


def employeView(request):

    data = Employee.objects.all()
    print(data)

    response = {'employees': list(data.values('name', 'sal'))}

    return JsonResponse(response)
