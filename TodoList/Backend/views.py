from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import TodoSerializer
# Create your views here.

class TodoList(APIView):
    def get(self,request):
        serializer = TodoSerializer(request.data)
        return serializer.data
    def post(self,request):
        pass
