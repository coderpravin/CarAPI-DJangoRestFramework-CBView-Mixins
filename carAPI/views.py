from django.shortcuts import render
from car.models import Car
from .serializers import CarSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
# Create your views here.

class CarViewAPI(APIView):
    def get(self, request):
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetailAPI(APIView):
    def get_object(self,pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist():
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def patch(self,request,pk):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(Self,request,pk):
        car = Car.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#using Mixins
class CarViewAPIMixin(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class CarDetailAPIMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,  generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self,request,pk):
        return self.retrieve(request, pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
    
