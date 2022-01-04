from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView
from django.http import Http404

from rest_framework import generics, mixins
from rest_framework import viewsets

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# FILTER
from django_filters.rest_framework import DjangoFilterBackend

# SEARCH
from rest_framework import filters


# Create your views here.

# viewSet (even more simple)


class StudentPaginations(PageNumberPagination):  # amount of recourds for page if I use LimitOffset dont create this.
    page_size = 2


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  

    # pagination_class = StudentPaginations
    pagination_class = LimitOffsetPagination

    # filter_backends = [DjangoFilterBackend] #FILTER
    # filterset_fields = ['name', 'score']

    filter_backends = [filters.OrderingFilter] # ORDERfilter
    ordering_fields = []

    # filter_backends = [filters.SearchFilter] #SEARCH
    # search_fields = ['^name', '^score']
    # ^ (starts with)
    # + exact matches
    # @ full-text (just in PostgresSQL)
    # $ Regex search



"""
# Generic (more simple)

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Mixins

class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        # .list is inheret from  mixins.ListModelMixin
        return self.list(request)

    def post(self, request):
        return self.create(request)

# primary key operation


class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# Class based views
class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
