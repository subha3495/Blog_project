from django.shortcuts import render
from testapp.models import Book,Author
from rest_framework import generics
from testapp.serializers import AuthorSerilizer,BookSerilizer
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class AuthorListview(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizer

class AuthorURD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerilizer

class BookListview(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class BookURD(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer