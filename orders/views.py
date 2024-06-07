from django.shortcuts import render,redirect
from . import models
# Create your views here.
def car_order(request,id):
  car=models.Car.objects.get(pk=id)

  if car.quantity>0:
    order=models.Order()
    order.user=request.user
    order.car=car
    order.save()
    car.quantity-=1
    car.save()
    return redirect('profile')

