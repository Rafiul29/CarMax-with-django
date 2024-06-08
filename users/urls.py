from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('register/',views.register,name='register'),
   path('login/',views.UserLoginView.as_view(),name='login'),
   path('profile/',views.Profile.as_view(),name='profile'),
   path('profile/edit',views.edit_profile,name='edit_profile'),
   path('profile/pass_chnage/',views.pass_chnage,name='pass_chnage'),
   path('logout/',views.UserLogoutView.as_view(),name='logout'),
]



