from django.db import models
from brands.models import Brand
# Create your models here.
class Car(models.Model):
  name=models.CharField(max_length=100)
  description=models.TextField()
  quantity=models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
  image=models.ImageField(upload_to='cars/images',default='cars/images/default.png')

  def __str__(self) -> str:
    return self.name
  
class Comment(models.Model):
  car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comments')
  name=models.CharField(max_length=30)
  email=models.EmailField()
  body=models.TextField()
  created_on=models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return f'comment by {self.name}'
