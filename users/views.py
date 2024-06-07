from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

# Create your views here.
def register(request):
  if request.method=='POST':
    register_form=forms.RegistrationForm(request.POST)
    if register_form.is_valid():
      print(register_form.cleaned_data)
      register_form.save()
      return redirect("register")
  else:
    register_form=forms.RegistrationForm()
  return render(request,'forms.html',{'form':register_form,'type':"Register"})


def user_login(request):
  if request.method=='POST':
    login_form=AuthenticationForm(request,data=request.POST)
    if login_form.is_valid():
      user_name=login_form.cleaned_data['username']
      user_password=login_form.cleaned_data['password']
      user=authenticate(username=user_name,password=user_password)
      if user is not None:
        login(request,user)
        messages.success(request, 'Logged in Successfully')
        return redirect('profile')
    else:
      messages.warning(request, 'Login informtion incorrect')
      return redirect('profile')
  else:
    login_form=AuthenticationForm()
  return render(request,'forms.html',{'form':login_form,'type':"Login"})

def profile(request):
  return render(request,'profile.html')

def user_logout(request):
  logout(request)
  return redirect('login')
