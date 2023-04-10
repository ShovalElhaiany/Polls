from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.request import Request
# from rest_framework import generics


class BooksView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorsView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('library:books-list', request=request, format=format),
        'authors': reverse('library:authors-list', request=request, format=format)
    })


"""Another way to create an api view"""
# class BookApi(generics.GenericAPIView, CreateModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin, generics.):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class AuthorApi(generics.GenericAPIView, CreateModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

"""Another way to create an api view"""
# class BookApi(generics.CreateAPIView, generics.DestroyAPIView, generics.ListAPIView, generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class AuthorApi(generics.CreateAPIView, generics.DestroyAPIView, generics.ListAPIView, generics.UpdateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
