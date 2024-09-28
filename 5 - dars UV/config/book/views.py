from .models import Genre, Author, Book
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, RetrieveUpdateAPIView)
from .serializers import GenreSerializer, AuthorSerializer, BookSerializer

# Create your views here.


class GenreApiView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailApiView(RetrieveUpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

#-----------------------------------------------

class AuthorApiView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailApiView(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

#-----------------------------------------------

class BookApiView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



