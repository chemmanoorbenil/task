from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from.models import Art
from .serializers import Artserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','POST'])
def article_list(request):

    if request.method =='GET':
        art = Art.objects.all()
        serializers=Artserializers(art,many=True)
        return  Response(serializers.data)

    elif request.method == 'POST':
        serializers=Artserializers(data=request.data)
        if serializers.is_valid():
              serializers.save()
              return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def art_detail(request,pk):
    try:
        art = Art.objects.get(pk=pk)

    except Art.DoesNotExist:
         return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    if request.method =='GET':
        Serializer = Artserializers(art)
        return Response(Serializer.data)


    elif request.method =='PUT':

        serializers=Artserializers(art,data=request.data)
        if serializers.is_valid():
             serializers.save()
             return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



