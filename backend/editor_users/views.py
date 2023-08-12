from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from .serializers import *
# Create your views here.
    
# detail = [ {"title": detail.title,"content": detail.content} for detail in EditorUsers.objects.all()]
class EditorUsersView(APIView):
    serializer_class = EditorUsersSerializer
    def get(self, request):
        detail_content = []
        count = 0
        for detail in EditorUsers.objects.all():
            print(detail)
            detail_content_list = detail.content.split(".")
            print(detail_content_list)
            for i in detail_content_list:
                detail_content += [{"title": f'{detail.title}{count}',"content": i}]
                count+=1
        detail = [ {"title": detail.title,"content": detail_content} for detail in EditorUsers.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = EditorUsersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

