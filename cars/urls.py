from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/<int:id>/',views.DetailCarView.as_view(),name='car_details'),
]


