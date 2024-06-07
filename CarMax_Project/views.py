from django.shortcuts import render
from cars.models import Car
from brands.models import Brand
# Create your views here.
def home(request):
  cars=Car.objects.all()
  brands=Brand.objects.all()
  return render(request,'home.html',{'cars':cars,'brands':brands})