from django.shortcuts import render
from django.http import JsonResponse
from .models import Car
# Create your views here.

def CarView(request):
    car = Car.objects.all().values()
    car = list(car)
    return JsonResponse(car, safe=False)
