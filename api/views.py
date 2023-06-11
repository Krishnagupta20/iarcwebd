from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Public,Name
from .serializers import PublicSerializer, NameSerializer

# Create your views here.
class PublicViewSet(generics.ListCreateAPIView):
    serializer_class=PublicSerializer
    queryset=Public.objects.all()

class PublicView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PublicSerializer
    queryset=Public.objects.all()
    




class NameList(generics.ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


class NameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
