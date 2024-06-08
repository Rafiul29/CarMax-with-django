from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
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

# @login_required
# def show_orders(request):
#   orders=models.Order.objects.filter(user=request.user)
#   return render(request,'order_history.html',{'orders':orders})


@method_decorator(login_required ,name="dispatch")
class ShowOrderHistoryView(ListView):
    model = models.Order
    template_name = 'order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return models.Order.objects.filter(user=self.request.user)