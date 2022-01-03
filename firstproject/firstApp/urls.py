from django.urls import path, include
from firstApp import views

urlpatterns = [
    path("emps/", views.employeView)
]
