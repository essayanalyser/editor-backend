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
        detail_res = []
        for detail in EditorUsers.objects.all():
            detail_content = []
            count = 0
            print(detail)
            detail_content_list = detail.content.split(".")
            print(detail_content_list)
            for i in detail_content_list:
                detail_content += [{"title": f'{detail.title}{count}',"content": i}]
                count+=1
            detail_res += [ {"title": detail.title,"content": detail_content} ]
        return Response(detail_res)
    
    def post(self, request):
        serializer = EditorUsersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    # def get(self, request, id):
    #     user_list_data = []
    #     for detail in EditorUsers.objects.all():
    #         if detail.title == id:
    #             user_list_data += [{"content":detail.content}] 
    #     return Response(user_list_data)
