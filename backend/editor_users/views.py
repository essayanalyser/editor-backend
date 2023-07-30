from django.shortcuts import render
from .serializers import EditorUsersSerializer 
from rest_framework import viewsets      
from .models import EditorUsers                 

class EditorUsersView(viewsets.ModelViewSet):  
    serializer_class = EditorUsersSerializer   
    queryset = EditorUsers.objects.all()    
