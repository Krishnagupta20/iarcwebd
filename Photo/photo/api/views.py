from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Public
from .serializers import PublicSerializer

# Create your views here.
class PublicViewSet(generics.ListCreateAPIView):
    serializer_class=PublicSerializer
    queryset=Public.objects.all()

class PublicView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PublicSerializer
    queryset=Public.objects.all()
     