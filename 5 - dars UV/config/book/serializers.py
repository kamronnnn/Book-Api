from rest_framework.serializers import ModelSerializer
from .models import Genre, Author, Book


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
