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
            sentences = []
            count = 0
            para = 0
            # print(detail.data)
            # print(detail)
            detail_content_list = detail.content.split(".")
            # print(detail_content_list)
            for i in detail_content_list:
                if '<p>' in i or '</p>' in i:
                    if '<p>' in i:
                        para+=1
                        count=0
                        sentences = []
                    newStr = i.replace("<p>","</p>")
                    newStr1 = newStr.replace("</p>",'').strip()
                    sentences += [{"sentence_id":count,"content":newStr1}]
                    # detail_content += [{"para":para,"sentences": sentences}]
                else:
                    sentences += [{"sentence_id":count,"content":i.strip()}]
                if count == 0:
                    detail_content += [{"para":para,"sentences": sentences}]
                count+=1
            
            detail_res += [ {"title": detail.title,"version": detail.version,"content": detail_content} ]
        user_list_data = []
        for detail in detail_res:
            if detail["title"] == title:
                user_list_data += [{"version":detail["version"],"content":detail["content"]}] 
        return Response(user_list_data)

    
    def post(self,request):
        print(request.data)
        json = HistoryDataSerializer(data=request.data)
        # for detail in HistoryData.objects.all():
            # print(detail.data)
        if json.is_valid(raise_exception=True):
            json.save()
            return Response(json.data)
        # serializer = EditorUsersSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        #     return Response(serializer.data)
        
    # def get_request(self, request, id):
    #     user_list_data = []
    #     for detail in EditorUsers.objects.all():
    #         if detail.title == id:
    #             user_list_data += [{"content":detail.content}] 
    #     return Response(user_list_data)
class HistoryDataView(APIView):
    serializer_class = HistoryDataSerializer
    def get(self, request, key):
        # my_versions = []
        detail_res = []
        for detail in HistoryData.objects.all():
            detail_content = []
            sentences = []
            count = 0
            para = 0
            # print(detail.data)
            # print(detail)
            detail_content_list = detail.data["content"].split(".")
                # print(detail_content_list)
            for i in detail_content_list:
                if '<p>' in i or '</p>' in i:
                    if '<p>' in i:
                        para+=1
                        count=0
                        sentences = []
                    newStr = i.replace("<p>","</p>")
                    newStr1 = newStr.replace("</p>",'').strip()
                    sentences += [{"sentence_id":count,"content":newStr1}]
                        # detail_content += [{"para":para,"sentences": sentences}]
                else:
                    sentences += [{"sentence_id":count,"content":i.strip()}]
                if count == 0:
                    detail_content += [{"para":para,"sentences": sentences}]
                count+=1
            
            detail_res += [ {"title": detail.key.title,"doc_name":detail.doc_name,"version": detail.data["version"],"content": detail_content} ]
        user_list_data = []
        for detail in detail_res:
            if detail["title"] == key:
                user_list_data += [{"doc_name":detail["doc_name"],"version":detail["version"],"content":detail["content"]}] 
        return Response(user_list_data)



        # for detail in HistoryData.objects.all():
        #     print(detail.key.title)
        #     if detail.key.title == key:
        #         my_versions += [{"version":detail.data["version"],"content":detail.data["content"]}]
        
