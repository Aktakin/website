from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodosSerializer
from .models import Todos

# Create your views here.

@api_view()
def todolist(request):
    queryset = Todos.objects.all()
    serializer = TodosSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def tododetail(request,id):
    todo = Todos.objects.get(pk=id)
    serializer = TodosSerializer(todo)
    return Response(serializer.data)