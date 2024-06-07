from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('create/<int:id>/',views.car_order ,name='car_order'),
]