from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.http import HttpResponse
from .models import Intake

# Create your views here.
class Intakelist(viewsets.ModelViewSet):
    queryset = Intake.objects.all()
    serializer_class = Intakeserializers
@api_view(['GET', 'PUT', 'DELETE'])
def Intake_detail(request, id):
    try:
        Intakes = Intake.objects.get(id=id)
    except Intakes.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Intakeserializers(Intakes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Intakeserializers(Intake, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Intakes.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)