from django.shortcuts import render
from rest_framework import generics
from .serializers import PlantSerializer, BlogSerializer, UserSerializer
from .models import Plant, Blog, User
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status
from django.conf import settings
# Create your views here.


class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser, )

    def post(self, request):
        print(request.FILES)
        plant_serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if plant_serializer.is_valid():
            plant_serializer.save()
            return Response(plant_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(plant_serializer)
            return Response(plant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = (MultiPartParser, FormParser)


class BlogList(generics.ListCreateAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
