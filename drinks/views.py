from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
        drink = Drink.objects.all()
        serializer =  DrinkSerializer(drink, many=True)
        return JsonResponse({"drinks":serializer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    


@api_view(['GET', 'POST','DELETE','PUT',])
def drink_detail(request,name):

    try:
        Vname = Drink.objects.get(pk=name)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
         serializer = DrinkSerializer(Vname)
         return Response(serializer.dat)
    elif request.method == 'DELETE':
        Vname.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        pass
    elif request.method == 'PUT':
         serializer = DrinkSerializer(Vname, data=request.data)
         if serializer.is_valid:
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
