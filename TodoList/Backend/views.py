from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import TodoViewSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class TodoListView(APIView):
    def get(self,request):
        serializer = TodoViewSerializer(data=request)
        if serializer.is_valid():
            return Response(serializer.data,status = status.HTTP_200_OK)
        print(serializer.data)
    