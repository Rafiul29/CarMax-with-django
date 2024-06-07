from django import forms
from .models import Car,Comment




class CommentForm(forms.ModelForm):
  class Meta:
    model=Comment
    fields=['name','email','body']
