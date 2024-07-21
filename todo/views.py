from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerialazer
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todo_serializer = TodoSerialazer(todos, many=True)
        return Response(todo_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerialazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)
