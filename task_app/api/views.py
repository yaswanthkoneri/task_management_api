from django.shortcuts import render
from task_app.api.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from task_app.models import Task
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters
from django.db.models import Q

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list(request):
    if request.method == 'GET':
        search_query = request.query_params.get('q', None)
        print('search_query', search_query)
        if search_query:
            tasks = Task.objects.filter(Q(name__icontains=search_query) 
                                    | Q(description__icontains=search_query))
        else:
            tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    if request.method == 'GET':
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT': 
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
    if request.method == 'DELETE':
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(data={'ok': 'deleted'})
    