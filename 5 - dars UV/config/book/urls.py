from django.urls import path
from .views import (GenreApiView, GenreDetailApiView,
                    AuthorApiView, AuthorDetailApiView, BookApiView, BookDetailApiView)

urlpatterns = [
    path('genre/', GenreApiView.as_view()),
    path('genre/<int:pk>/', GenreDetailApiView.as_view()),

    path('author/', AuthorApiView.as_view()),
    path('author/<int:pk>/', AuthorDetailApiView.as_view()),

    path('book/', BookApiView.as_view()),
    path('book/<int:pk>/', BookDetailApiView.as_view()),
]
