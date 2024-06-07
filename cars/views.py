from django.shortcuts import render,redirect
from . import models
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from . import forms
# Create your views here.

class DetailCarView(DetailView):
  model=models.Car
  pk_url_kwarg='id'
  template_name='car_details.html'

  def post(self, request, *args, **kwargs):
      comment_form = forms.CommentForm(data=self.request.POST)
      car = self.get_object()
      if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
      return self.get(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    car=self.object
    comments=car.comments.all()
    comment_form=forms.CommentForm()
    context['comments']=comments
    context['comment_form']=comment_form
    return context


def delete_comment(request,id):
  form=models.Comment.objects.get(pk=id).delete()
  return redirect('profile')