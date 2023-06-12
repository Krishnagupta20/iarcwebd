from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Public
from .serializers import PublicSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PublicViewSet(generics.ListCreateAPIView):
    serializer_class=PublicSerializer
    queryset=Public.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

class PublicView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=PublicSerializer
    queryset=Public.objects.all()
     