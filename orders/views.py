from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
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

@login_required
def show_orders(request):
  orders=models.Order.objects.filter(user=request.user)
  return render(request,'order_history.html',{'orders':orders})
