from .views import PublicView,PublicViewSet, NameDetail, NameList
from django.contrib import admin
from django.urls import path,include






urlpatterns = [
     path('public',PublicViewSet.as_view()),
    path('public/<int:pk>/',PublicView.as_view()),
    path('name/', NameList.as_view()),
    path('name/<int:pk>/', NameDetail.as_view()),
]