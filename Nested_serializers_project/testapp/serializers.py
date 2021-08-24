from testapp.models import Book,Author
from rest_framework import serializers

class BookSerilizer(serializers.ModelSerializer):
    class Meta():
        model  = Book
        fields = '__all__'

class AuthorSerilizer(serializers.ModelSerializer):
    books_by_author=BookSerilizer(read_only=True,many=True)
    class Meta():
        model  = Author
        fields = '__all__'