from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


@api_view(['GET','POST'])
def programacion_api_view(request):
    
    if request.method == 'GET':
        programacion_data = Programacion.objects.all()
        programacion_serializer = ProgramacionSerializer(programacion_data,many=True)
        return  Response(programacion_serializer.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        programacion_serializer = ProgramacionSerializer(data=request.data)
        if programacion_serializer.is_valid():
            programacion_serializer.save()
            return Response(request.data,status=status.HTTP_201_CREATED)
        return Response(programacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def programacion_api_view(request):

    if request.method == 'GET':
        return;
    if request.method == 'PUT':
        return;
    if request.method == 'DELETE':
        return;

    