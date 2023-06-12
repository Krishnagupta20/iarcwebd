from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Public,Name
from .serializers import PublicSerializer, NameSerializer
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
    




class NameList(generics.ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


class NameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
