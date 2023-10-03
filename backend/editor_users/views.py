from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from .serializers import *
# Create your views here.
    
# detail = [ {"title": detail.title,"content": detail.content} for detail in EditorUsers.objects.all()]
class EditorUsersView(APIView):
    serializer_class = EditorUsersSerializer
    def get(self, request, title):
        detail_res = []
        for detail in EditorUsers.objects.all():
            detail_content = []
            count = 0
            para = 0
            print(detail)
            detail_content_list = detail.content.split(".")
            print(detail_content_list)
            for i in detail_content_list:
                if '<p>' in i or '</p>' in i:
                    if '<p>' in i:
                        para+=1
                    newStr = i.replace("<p>","</p>")
                    newStr1 = newStr.replace("</p>",'')
                    detail_content += [{"title": f'{detail.title}p{para}s{count}',"content": newStr1}]
                else:
                    detail_content += [{"title": f'{detail.title}p{para}s{count}',"content": i}]
                count+=1
            detail_res += [ {"title": detail.title,"version": detail.version,"content": detail_content} ]
        user_list_data = []
        for detail in detail_res:
            if detail["title"] == title:
                user_list_data += [{"version":detail["version"]}] 
                user_list_data += [{"content":detail["content"]}] 
        return Response(user_list_data)

    
    def post(self, request):
        serializer = EditorUsersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    # def get_request(self, request, id):
    #     user_list_data = []
    #     for detail in EditorUsers.objects.all():
    #         if detail.title == id:
    #             user_list_data += [{"content":detail.content}] 
    #     return Response(user_list_data)
