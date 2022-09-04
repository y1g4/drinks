from pickle import GET
from telnetlib import STATUS
from urllib import response
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import  Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):

    #get all the drinks
    #serialize them
    #return json

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializers = DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks': serializers.data})

    if request.method == 'POST':
        serializers = DrinkSerializer(data=request.data)
        if serializers.is_valid():

            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def drink_details(request,id):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializers = DrinkSerializer(drink)
        return Response(serializers.data)
    elif request.method =='POST':
        pass
    elif request.method =="DELETE":
        pass
