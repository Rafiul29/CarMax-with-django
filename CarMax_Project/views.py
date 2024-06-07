from django.shortcuts import render
from cars.models import Car
from brands.models import Brand
# Create your views here.
def home(request,brand_slug=None):
  cars=Car.objects.all()
  brands=Brand.objects.all()
  if brand_slug is not None:
    brand=Brand.objects.get(slug=brand_slug)
    cars=Car.objects.filter(brand=brand)

  return render(request,'home.html',{'cars':cars,'brands':brands})