from .views import PublicView,PublicViewSet
from django.contrib import admin
from django.urls import path,include






urlpatterns = [
     path('public',PublicViewSet.as_view()),
    path('public/<int:pk>/',PublicView.as_view())
]