from django.shortcuts import render
from rest_framework.decorators import api_view
from . serializers import TodoViewSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Todo
# Create your views here.

@api_view(['GET'])
def todo_view(request):
    todos = Todo.objects.all()
    serializer = TodoViewSerializer(todos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def todo_add(request):
    serializer = TodoViewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])        
def todo_delete(request,pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
    except todo.DoesNotExist:
        return Response({"error": "Todo List not found"}, status=status.HTTP_404_NOT_FOUND)