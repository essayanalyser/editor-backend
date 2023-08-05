from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from .serializers import *
# Create your views here.

class EditorUsersView(APIView):
	
	serializer_class = EditorUsersSerializer

	def get(self, request):
		detail = [ {"title": detail.title,"content": detail.content}
		for detail in EditorUsers.objects.all()]
		return Response(detail)

	def post(self, request):
		serializer = EditorUsersSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)

