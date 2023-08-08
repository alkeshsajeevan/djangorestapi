from django.shortcuts import render
from  rest_framework.views import APIView
from .serializer import Foofserializer
from .models import Food
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class FoodList(APIView):



    def get(self,request):
        food=Food.objects.all()
        serializer=Foofserializer(food,many=True)
        return Response(serializer.data)




    def post(self,request):
     serializer=Foofserializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
     return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)


class FoodDetail(APIView):
   
   def get_food(self,pk):
      try:
         food=Food.objects.get(pk=pk)
         return food

      except:
         raise status.HTTP_404_NOT_FOUND
      
   def get(self,request,pk):
     
     food=self.get_food(pk=pk)
     serializer=Foofserializer(food)
     return Response(serializer.data,status=status.HTTP_200_OK)
   

   def delete(self,request,pk):
      food=self.get_food(pk=pk)
      food.delete()

      return Response (status=status.HTTP_204_NO_CONTENT)
   
   def put(self,request,pk):
      food=self.get_food(pk=pk)
      serializer=Foofserializer(food,request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)