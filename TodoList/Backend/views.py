from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import TodoViewSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Todo
# Create your views here.

class TodoListView(APIView):
    def post(self, request):
        serializer = TodoViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        todos = Todo.objects.all()
        serializer = TodoViewSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self,request,*args, **kwargs):
        try:
            todo = Todo.objects.filter(id=kwargs['pk'])
            serializer = TodoViewSerializer(todo, many=True)
        except Todo.DoesNotExist:
            return Response({"error": "Todo List not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK) 